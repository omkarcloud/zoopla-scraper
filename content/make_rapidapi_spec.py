import json
from pathlib import Path
from urllib.parse import urlsplit, urlunsplit

HERE = Path(__file__).parent
SRC = HERE / "openapi_spec.json"
DST = HERE / "rapidapi_spec.json"
METADATA = HERE / "rapidapi_metadata.md"
README = HERE / "rapidapi_readme.md"
BROWSER_JS = HERE / "browser_reorder.js"

# --- RapidAPI listing config (info block) -----------------------------------
# Required by the upload validator (MISSING_REQUIRED_PROP without it). Keep it
# equal to the live version's name so uploads update in place instead of
# spawning a new version.
VERSION = "1.0.0"                   # must equal the LIVE RapidAPI version name or the upload creates a new version
TERMS_OF_SERVICE = "https://www.omkar.cloud/legal/terms"
CONTACT = {"name": "Omkar Cloud", "url": "https://www.omkar.cloud", "email": "chetan@omkar.cloud"}


def derive_website(spec):
    """Tool playground URL from the source server host, e.g.
    'https://imdb-scraper.omkar.cloud' -> 'https://www.omkar.cloud/tools/imdb-scraper/playground'."""
    url = spec.get("servers", [{}])[0].get("url", "")
    host = urlsplit(url).netloc.split(":")[0]
    labels = host.split(".")
    domain = ".".join(labels[-2:])
    slug = labels[0]
    return f"https://www.{domain}/tools/{slug}/playground"

# --- browser_reorder.js config ----------------------------------------------
API_ID = "api_REPLACE_ME"          # Zoopla's RapidAPI api id (Studio URL) — needed only for browser_reorder.js
CSRF_TOKEN = "REPLACE_ME"          # from DevTools when running browser_reorder.js

# https://rapidapi.com/studio/api_c9b6baf6-4966-49c7-8539-2b33fed60d1d/publish/definitions
def common_prefix(paths):
    """Longest common leading segments across all paths, always leaving each
    path's final (endpoint) segment. E.g. '/aliexpress/v2/search' -> '/aliexpress/v2'."""
    split = [p.strip("/").split("/") for p in paths]
    if not split:
        return ""
    max_prefix = min(len(s) for s in split) - 1  # never consume the endpoint segment
    prefix = []
    for i, segments in enumerate(zip(*split)):
        if i >= max_prefix:
            break
        if len(set(segments)) == 1 and not segments[0].startswith("{"):
            prefix.append(segments[0])
        else:
            break
    return "/" + "/".join(prefix) if prefix else ""


def rewrite_host(url):
    """Collapse any subdomain into the gateway host, e.g.
    'https://aliexpress-scraper-api.omkar.cloud' -> 'https://api.omkar.cloud/rpi'."""
    parts = urlsplit(url)
    if not parts.netloc:
        return url
    domain = ".".join(parts.netloc.split(":")[0].split(".")[-2:])  # registrable domain
    netloc = "api." + domain
    path = "/rpi" + parts.path.rstrip("/")
    return urlunsplit((parts.scheme or "https", netloc, path, "", ""))


def site_from_host(url):
    """Module segment derived from the public host label, mirroring js-scraper's
    rule: 'imdb-scraper' / 'nike-scraper-api' / 'x-api' / 'x' -> 'imdb' / 'nike' / 'x'."""
    label = urlsplit(url).netloc.split(":")[0].split(".")[0]
    for suffix in ("-scraper-api", "-scraper", "-api"):
        if label.endswith(suffix) and len(label) > len(suffix):
            return label[: -len(suffix)]
    return label


def move_prefix_to_servers(spec):
    paths = spec.get("paths", {})
    if not paths:
        return ""
    prefix = common_prefix(paths)
    if prefix:
        spec["paths"] = {p[len(prefix):] or "/": v for p, v in paths.items()}
    else:
        # Prefix-less spec (new-style host such as imdb-scraper.omkar.cloud/title/details):
        # the module segment comes from the host label instead, and still has to be
        # part of the RapidAPI server URL because RapidAPI calls api.omkar.cloud/rpi/<site>.
        prefix = "/" + site_from_host(spec.get("servers", [{}])[0].get("url", ""))
    for server in spec.get("servers", []):
        server["url"] = rewrite_host(server["url"]).rstrip("/") + prefix
    return prefix


def detect_tag(spec, prefix):
    if prefix:
        return prefix.strip("/").split("/")[0].replace("-", " ").title()
    return spec.get("info", {}).get("title", "API")


def add_operation_ids(spec):
    for path_item in spec.get("paths", {}).values():
        for op in path_item.values():
            if isinstance(op, dict) and "summary" in op and "operationId" not in op:
                op["operationId"] = op["summary"]


def flatten_groups(spec, tag):
    for path_item in spec.get("paths", {}).values():
        for op in path_item.values():
            if isinstance(op, dict):
                op["tags"] = [tag]
    spec["tags"] = [{"name": tag}]


def convert(node):
    if isinstance(node, dict):
        if "enum" in node and "example" not in node:
            node["type"] = "string"
            del node["enum"]
        for value in node.values():
            convert(value)
    elif isinstance(node, list):
        for item in node:
            convert(item)


def parse_metadata():
    """Pull the short and long descriptions out of rapidapi_metadata.md."""
    sections = {}
    current = None
    for line in METADATA.read_text().splitlines():
        if line.startswith("# "):
            current = line[2:].split("(")[0].strip().lower()
            sections[current] = []
        elif current is not None:
            sections[current].append(line)
    short = "\n".join(sections.get("short description", [])).strip()
    long_ = "\n".join(sections.get("long description", [])).strip()
    return short, long_


def build_info(spec, website):
    """The info block RapidAPI reads its hub metadata from (x- extensions per
    https://docs.rapidapi.com/docs/adding-and-updating-openapi-documents).
    Intentionally NOT set (managed in the dashboard, not overwritten on upload):
    version, x-category, x-thumbnail.
    Note: x-version-lifecycle must be lowercase — the validator rejects ACTIVE."""
    short, long_ = parse_metadata()
    return {
        "title": spec["info"]["title"],
        "version": VERSION,
        "description": short,
        "termsOfService": TERMS_OF_SERVICE,
        "contact": CONTACT,
        "x-long-description": long_,
        "x-website": website,
        "x-public": True,
        "x-version-lifecycle": "active",
    }


def spec_lite(spec):
    """Just what browser_reorder.js needs: path order + param-name order."""
    paths = {}
    for route, path_item in spec.get("paths", {}).items():
        paths[route] = {
            method: {"parameters": [{"name": p["name"]} for p in op.get("parameters", [])]}
            for method, op in path_item.items()
            if isinstance(op, dict) and "responses" in op
        }
    return {"paths": paths}


BROWSER_JS_TEMPLATE = r"""// GENERATED by make_rapidapi_spec.py — do not edit by hand; edit the config
// at the top of make_rapidapi_spec.py and re-run it.
//
// RapidAPI endpoint + params reorder — paste into the browser console on a
// logged-in rapidapi.com tab (DevTools -> Console -> paste -> Enter).
//
// What it does, in order:
//   1. Fetches the version's endpoints with their params.
//   2. For EACH endpoint whose params are out of spec order, replays the
//      dashboard's updateEndpointWithParameters mutation with the params
//      re-indexed to match the spec (ids, descriptions, payloads preserved).
//   3. Reorders the endpoints themselves (updateEndpointsCollectionOrder).
//   4. Re-fetches and prints the final state.
//
// If calls fail with 401/403, refresh CSRF_TOKEN in make_rapidapi_spec.py
// (DevTools -> Network -> any "graphql" request -> request headers ->
// csrf-token) and regenerate, or just edit the constant below.

(async () => {
  const API_ID = '__API_ID__';
  const CSRF_TOKEN = '__CSRF_TOKEN__';
  const API_VERSION_ID = ''; // optional; empty = use the current version
  const DRY_RUN = false; // true = only print what would change
  const SPEC = __SPEC_JSON__;

  if (!/^api_/.test(API_ID)) throw new Error('API_ID is still the stub. Paste your real api_... id.');
  if (!CSRF_TOKEN || CSRF_TOKEN.length < 10) throw new Error('CSRF_TOKEN is still the stub.');
  if (typeof SPEC !== 'object' || !SPEC.paths || !Object.keys(SPEC.paths).length) {
    throw new Error('SPEC is still the stub. It must be an object with a non-empty "paths" key.');
  }

  const desiredOrder = Object.keys(SPEC.paths);

  const stripTypename = (v) => {
    if (Array.isArray(v)) return v.map(stripTypename);
    if (v && typeof v === 'object') {
      const out = {};
      for (const [k, val] of Object.entries(v)) if (k !== '__typename') out[k] = stripTypename(val);
      return out;
    }
    return v;
  };

  const gql = async (operationName, query, variables) => {
    const res = await fetch('https://rapidapi.com/gateway/graphql', {
      method: 'POST',
      credentials: 'include',
      headers: {
        accept: '*/*',
        'content-type': 'application/json',
        'csrf-token': CSRF_TOKEN,
        'rapid-client': 'provider-dashboard-service',
      },
      body: JSON.stringify({ operationName, variables, extensions: {}, query }),
    });
    if (!res.ok) throw new Error(`HTTP ${res.status}: ${(await res.text()).slice(0, 300)}`);
    const json = await res.json();
    if (json.errors && json.errors.length) throw new Error('GraphQL errors: ' + JSON.stringify(json.errors, null, 2));
    return json.data;
  };

  const resolveVersionId = async () => {
    if (API_VERSION_ID) return API_VERSION_ID;
    const data = await gql(
      'getVersions',
      `query getVersions($apiId: ID!) { api(id: $apiId) { id name versions { id name current versionStatus } } }`,
      { apiId: API_ID }
    );
    const v = data.api.versions.find((x) => x.current);
    if (!v) throw new Error('Could not resolve a current version — set API_VERSION_ID.');
    console.log(`API: ${data.api.name} — using current version ${v.name} (${v.id})`);
    return v.id;
  };

  const fetchEndpoints = async (apiVersionId) => {
    const data = await gql(
      'GetDataForEndpoints',
      `query GetDataForEndpoints($apiVersionId: ID!) {
        apiVersion(apiVersionId: $apiVersionId) {
          id
          endpoints(pagingArgs: {limit: -1}) {
            id index method name route description group
            response displayResponse isMockResponse mockResponseId
            params { optional required headers constant }
            responsePayloads { id name format body headers description status statusCode examples schema }
            requestPayloads { id name format body description examples schema }
            externalDocs { description url }
          }
        }
      }`,
      { apiVersionId }
    );
    return stripTypename(data.apiVersion.endpoints).sort((a, b) => a.index - b.index);
  };

  // Build the params.route entry shape the dashboard sends in
  // updateEndpointWithParameters (drop createdAt/updatedAt/endpoint/type).
  const toRouteParam = (p, index) => {
    const out = {
      index,
      id: p.id,
      name: p.name,
      querystring: p.querystring,
      paramType: p.paramType,
      condition: p.condition,
      description: p.description,
      status: p.status,
      schema: p.schema,
      schemaDefinition: p.schemaDefinition,
    };
    if (p.value !== undefined) out.value = p.value;
    return out;
  };

  const specParamNames = (route) => {
    const item = SPEC.paths[route] || {};
    const op = item.get || item.post || Object.values(item)[0] || {};
    return (op.parameters || []).map((p) => p.name);
  };

  // Reorder one endpoint's route params to spec order; returns null if already ordered.
  const buildParamsUpdate = (e) => {
    const live = [...(e.params?.required || []), ...(e.params?.optional || [])];
    if ((e.params?.constant || []).length) {
      console.warn(`  ${e.route}: has CONSTANT params — leaving them untouched (not supported by this script).`);
    }
    if (!live.length) return null;

    const wanted = specParamNames(e.route);
    const byName = new Map(live.map((p) => [p.name, p]));
    const ordered = wanted.filter((n) => byName.has(n)).map((n) => byName.get(n));
    const leftovers = live.filter((p) => !wanted.includes(p.name));
    if (leftovers.length) {
      console.warn(`  ${e.route}: params not in spec, appending at end: ${leftovers.map((p) => p.name).join(', ')}`);
    }
    const finalList = [...ordered, ...leftovers];
    const changed = finalList.some((p, i) => p.index !== i);
    if (!changed) return null;

    return {
      name: e.name,
      description: e.description,
      externalDocs: e.externalDocs || {},
      apiVersionId: undefined, // filled by caller
      params: {
        route: finalList.map(toRouteParam),
        header: (e.params?.headers || []).map(toRouteParam),
      },
      payloadParameters: [],
      method: e.method,
      displayResponse: e.displayResponse ?? false,
      response: e.response ?? '',
      responsePayloads: (e.responsePayloads || []).map((p) => ({
        id: p.id,
        name: p.name,
        format: p.format,
        body: p.body ?? '',
        headers: p.headers ?? '{}',
        description: p.description,
        status: p.status,
        statusCode: p.statusCode,
        examples: p.examples,
        schema: p.schema,
      })),
      requestPayloads: e.requestPayloads || [],
      mockResponseId: e.mockResponseId ?? null,
      route: e.route,
      routeregex: e.route,
      endpointId: e.id,
    };
  };

  const updateEndpointParams = (input) =>
    gql(
      'updateEndpointWithParameters',
      `mutation updateEndpointWithParameters($input: updateOrCreateEndpointWithParameters!) {
        updateOrCreateEndpointWithParameters(input: $input)
      }`,
      { input }
    );

  const reorderEndpoints = (plan) =>
    gql(
      'updateEndpointsCollectionOrder',
      `mutation updateEndpointsCollectionOrder($endpointsCollectionOrder: [EndpointOrder]) {
        updateEndpointsCollectionOrder(endpointsCollectionOrder: $endpointsCollectionOrder)
      }`,
      { endpointsCollectionOrder: plan }
    );

  const printState = (endpoints) => {
    console.table(
      endpoints.map((e) => ({
        index: e.index,
        route: e.route,
        params: [...(e.params?.required || []), ...(e.params?.optional || [])]
          .sort((a, b) => a.index - b.index)
          .map((p) => p.name)
          .join(', '),
      }))
    );
  };

  // ------------------------------ run --------------------------------------
  const apiVersionId = await resolveVersionId();
  const endpoints = await fetchEndpoints(apiVersionId);
  console.log('Current state:');
  printState(endpoints);

  const byRoute = new Map(endpoints.map((e) => [e.route, e]));
  const missing = desiredOrder.filter((r) => !byRoute.has(r));
  if (missing.length) throw new Error(`Spec routes not found in this version: ${missing.join(', ')}`);
  const extra = endpoints.filter((e) => !desiredOrder.includes(e.route));
  if (extra.length) throw new Error(`Endpoints not in spec: ${extra.map((e) => e.route).join(', ')}`);

  // Step 1: per-endpoint param reorder.
  console.log('\nStep 1 — params:');
  let paramUpdates = 0;
  for (const route of desiredOrder) {
    const e = byRoute.get(route);
    const input = buildParamsUpdate(e);
    if (!input) {
      console.log(`  ${route}: params already in spec order`);
      continue;
    }
    input.apiVersionId = apiVersionId;
    const order = input.params.route.map((p) => p.name).join(', ');
    if (DRY_RUN) {
      console.log(`  ${route}: WOULD reorder params -> ${order}`);
    } else {
      await updateEndpointParams(input);
      console.log(`  ${route}: params reordered -> ${order}`);
    }
    paramUpdates++;
  }
  if (!paramUpdates) console.log('  nothing to do');

  // Step 2: endpoint order.
  const endpointPlan = desiredOrder.map((route, index) => ({ endpointId: byRoute.get(route).id, index }));
  const endpointChanges = desiredOrder.filter((route, i) => byRoute.get(route).index !== i);
  console.log(`\nStep 2 — endpoint order: ${endpointChanges.length} of ${endpointPlan.length} need moving`);
  if (endpointChanges.length && !DRY_RUN) {
    await reorderEndpoints(endpointPlan);
    console.log('  applied');
  }

  // Step 3: verify.
  if (!DRY_RUN) {
    console.log('\nFinal state:');
    printState(await fetchEndpoints(apiVersionId));
  } else {
    console.log('\nDRY_RUN was on — nothing was changed.');
  }
})();
"""


def emit_browser_js(spec):
    js = (
        BROWSER_JS_TEMPLATE
        .replace("__API_ID__", API_ID)
        .replace("__CSRF_TOKEN__", CSRF_TOKEN)
        .replace("__SPEC_JSON__", json.dumps(spec_lite(spec), indent=2))
    )
    BROWSER_JS.write_text(js)


spec = json.loads(SRC.read_text())
website = derive_website(spec)  # from the original server host, before rewrite
convert(spec)
prefix = move_prefix_to_servers(spec)
add_operation_ids(spec)
flatten_groups(spec, detect_tag(spec, prefix))
info = build_info(spec, website)
spec = {"openapi": spec.get("openapi", "3.0.0"), "info": info, "servers": spec.get("servers", []),
        "paths": spec["paths"], "tags": spec["tags"],
        "x-documentation": {"readme": README.read_text()}}
DST.write_text(json.dumps(spec, indent=2, ensure_ascii=False) + "\n")
print(f"Wrote {DST}")
emit_browser_js(spec)
print(f"Wrote {BROWSER_JS}")

# python make_rapidapi_spec.py
