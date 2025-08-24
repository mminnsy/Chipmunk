import pandas as pd
from datetime import datetime
import os

# Assume the CSV is in the repo's root for GitHub Actions; adjust the path if running locally
csv_filename = "Matchbook_Filter.csv"
if not os.path.exists(csv_filename):
    # Create a placeholder if the CSV isn't present for demonstration
    tips = [{"Notice": "CSV file not found."}]
else:
    df = pd.read_csv(csv_filename)
    tips = df.head(10).to_dict(orient='records')

html_content = f"""<!DOCTYPE html>
<html>
  <head>
    <meta name="robots" content="noindex, nofollow">
    <title>Daily Horse Matchbook Tips</title>
  </head>
  <body>
    <h1>Daily Horse Matchbook Tips: {datetime.now():%Y-%m-%d}</h1>
    <ul>
    {''.join(f"<li>{', '.join(f'{k}: {v}' for k, v in tip.items())}</li>" for tip in tips)}
    </ul>
  </body>
</html>
"""

with open('index.html', 'w', encoding='utf-8') as file:
    file.write(html_content)
