function tsToIso(ts) {
  if (ts == null) return null;
  return new Date(ts).toISOString();
}

function extractTrackingInfo(response) {
  const module = (response.module && response.module[0]) || {};

  const processInfo = module.processInfo || {};
  const latestTrace = module.latestTrace || {};
  const detailList = module.detailList || [];

  const events = detailList.map(d => ({
    timestamp: d.time ?? null,
    time_iso: tsToIso(d.time),
    description: d.desc ?? null,
    standard_description: d.standerdDesc ?? null,
    action_code: d.actionCode ?? null,
    timezone: d.timeZone ?? null,
    node: d.group?.nodeDesc ?? null
  }));


  events.sort((a, b) => (a.timestamp || 0) - (b.timestamp || 0));

  return {
    tracking_number: module.mailNo ?? null,
    origin_country: module.originCountry ?? null,
    destination_country: module.destCountry ?? null,
    status: module.status ?? null,
    status_description: module.statusDesc ?? null,
    progress_rate: processInfo.progressRate ?? null,
    progress_percent:
      processInfo.progressRate != null
        ? Math.round(processInfo.progressRate * 1000) / 10
        : null,
    latest_event: {
      timestamp: latestTrace.time ?? null,
      time_iso: tsToIso(latestTrace.time),
      description: latestTrace.desc ?? null,
      standard_description: latestTrace.standerdDesc ?? null,
      action_code: latestTrace.actionCode ?? null,
      node: latestTrace.group?.nodeDesc ?? null
    },
    event_history: events,
    days_in_transit: module.daysNumber ?? null
  };
}

function fetchTrackingNumbers() {
  return {
    1: { item: "Item 1", link: "TRACKING_NUMBER_HERE" },
    2: { item: "Item 2", link: "TRACKING_NUMBER_HERE" },
    3: { item: "Item 3", link: "TRACKING_NUMBER_HERE" }
  };
}

async function main() {
  const trackingNumbers = fetchTrackingNumbers();

  for (const entry of Object.values(trackingNumbers)) {
    const code = entry.link;
    const url = `https://global.cainiao.com/global/detail.json?mailNos=${code}&lang=en-US&language=en-US`;

    const res = await fetch(url);
    if (!res.ok) {
      console.error(`Request failed for ${code}: ${res.status}`);
      continue;
    }

    const response = await res.json();
    const prettyResponseData = extractTrackingInfo(response);

    console.dir(prettyResponseData, { depth: null });


  }
}

main().catch(err => {
  console.error("Fatal error:", err);
});
