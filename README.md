# Cainiao / AliExpress / Alibaba Tracking Parser  
**Python & JavaScript**

This project fetches shipment tracking data from Cainiao (used by AliExpress, Alibaba, Temu, etc.) and converts the undocumented, inconsistent API response into a clean, normalised structure suitable for:

- APIs
- Databases
- Dashboards
- Automation
- Paid microservices

This repo contains **two equivalent implementations**:
- Python (reference implementation)
- JavaScript (Node.js)

Both produce the same structured output.

---

## What This Actually Does (No Marketing BS)

Cainiao returns deeply nested, poorly structured JSON.

This project:
- Normalises timestamps
- Sorts events oldest → newest
- Extracts meaningful shipment metadata
- Calculates progress percentage
- Outputs clean, predictable JSON

This is **data infrastructure**, not a demo script.

---

## API Source

All data is fetched from:

```

https://global.cainiao.com/global/detail.json

```

Example request:
```

?mailNos=TRACKING_NUMBER&lang=en-US&language=en-US

````

⚠️ This endpoint is **undocumented** and may change without notice.

---

## Requirements

### Python
- Python **3.9+**
- `requests`

### JavaScript
- Node.js **18+**
- No external dependencies (uses built-in `fetch`)

---

## Python Usage

### 1. Install dependencies

```bash
pip install requests
````

### 2. Save the file

Save your Python script as:

```bash
main.py
```

### 3. Add tracking numbers

Edit `fetch_tracking_numbers()`:

```python
def fetch_tracking_numbers():
    return {
        1: {"item": "Item 1", "link": "TRACKING_NUMBER_HERE"}
    }
```

### 4. Run it

```bash
python main.py
```

### 5. Output

Each tracking number produces structured output like:

```json
{
  "tracking_number": "AP00780065527911",
  "origin_country": "CN",
  "destination_country": "GB",
  "status": "DELIVERING",
  "progress_percent": 62.5,
  "latest_event": {
    "time_iso": "2026-01-19T09:41:00Z",
    "description": "Arrived at local delivery center"
  },
  "event_history": [...]
}
```

---

## JavaScript Usage (Node.js)

### 1. Save the file

```bash
script.js
```

### 2. Add tracking numbers

Edit `fetchTrackingNumbers()`:

```js
function fetchTrackingNumbers() {
  return {
    1: { item: "Item 1", link: "TRACKING_NUMBER_HERE" }
  };
}
```

### 3. Run it

```bash
node script.js
```

---

## Output Format (Both Versions)

Both implementations return **identical structure**:

* `tracking_number`
* `origin_country`
* `destination_country`
* `status`
* `status_description`
* `progress_rate`
* `progress_percent`
* `latest_event`
* `event_history` (sorted)
* `days_in_transit`


---




## License

MIT License

Copyright (c) Odin Bryant

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
