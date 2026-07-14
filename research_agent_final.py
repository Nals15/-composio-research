"""
Composio App Research Agent
============================
Researches 100 apps for AI agent buildability using:
- Composio SDK (composio-core) for toolkit initialization and tool listing
- Groq API (Llama 3.3 70B) as the LLM brain for research
- Python 3.12 (required — composio-core has pysher dependency incompatible with 3.13)

Usage:
    py -3.12 research_agent_final.py
"""

from composio import Composio
from groq import Groq
import json
import time
import csv

# --- CONFIGURATION ---
GROQ_API_KEY = "your GROQ API KEY"
COMPOSIO_API_KEY = "your COMPOSIO API KEY"

# Initialize Composio client
composio_client = Composio(api_key=COMPOSIO_API_KEY)

# Initialize Groq client  
groq_client = Groq(api_key=GROQ_API_KEY)

# Log Composio connection
print("Connecting to Composio...")
try:
    apps = composio_client.apps.get()
    print(f"Composio connected. {len(apps)} apps available in Composio toolkit.")
except Exception as e:
    print(f"Composio connection note: {str(e)[:100]}")
    print("Continuing with research agent...")

print()

# --- 100 APPS LIST ---
research_apps = [
    {"id": 1, "name": "Salesforce", "url": "salesforce.com", "category": "CRM and Sales"},
    {"id": 2, "name": "HubSpot", "url": "hubspot.com", "category": "CRM and Sales"},
    {"id": 3, "name": "Pipedrive", "url": "pipedrive.com", "category": "CRM and Sales"},
    {"id": 4, "name": "Attio", "url": "attio.com", "category": "CRM and Sales"},
    {"id": 5, "name": "Twenty", "url": "twenty.com", "category": "CRM and Sales"},
    {"id": 6, "name": "Podio", "url": "podio.com", "category": "CRM and Sales"},
    {"id": 7, "name": "Zoho CRM", "url": "zoho.com/crm", "category": "CRM and Sales"},
    {"id": 8, "name": "Close", "url": "close.com", "category": "CRM and Sales"},
    {"id": 9, "name": "Copper", "url": "copper.com", "category": "CRM and Sales"},
    {"id": 10, "name": "DealCloud", "url": "api.docs.dealcloud.com", "category": "CRM and Sales"},
    {"id": 11, "name": "Zendesk", "url": "zendesk.com", "category": "Support and Helpdesk"},
    {"id": 12, "name": "Intercom", "url": "intercom.com", "category": "Support and Helpdesk"},
    {"id": 13, "name": "Freshdesk", "url": "freshdesk.com", "category": "Support and Helpdesk"},
    {"id": 14, "name": "Front", "url": "front.com", "category": "Support and Helpdesk"},
    {"id": 15, "name": "Pylon", "url": "usepylon.com", "category": "Support and Helpdesk"},
    {"id": 16, "name": "LiveAgent", "url": "liveagent.com", "category": "Support and Helpdesk"},
    {"id": 17, "name": "Plain", "url": "plain.com", "category": "Support and Helpdesk"},
    {"id": 18, "name": "Help Scout", "url": "helpscout.com", "category": "Support and Helpdesk"},
    {"id": 19, "name": "Gorgias", "url": "gorgias.com", "category": "Support and Helpdesk"},
    {"id": 20, "name": "Gladly", "url": "gladly.com", "category": "Support and Helpdesk"},
    {"id": 21, "name": "Slack", "url": "slack.com", "category": "Communications and Messaging"},
    {"id": 22, "name": "Twilio", "url": "twilio.com", "category": "Communications and Messaging"},
    {"id": 23, "name": "Zoho Cliq", "url": "zoho.com/cliq", "category": "Communications and Messaging"},
    {"id": 24, "name": "Lark", "url": "open.larksuite.com", "category": "Communications and Messaging"},
    {"id": 25, "name": "Pumble", "url": "pumble.com", "category": "Communications and Messaging"},
    {"id": 26, "name": "Discord", "url": "discord.com", "category": "Communications and Messaging"},
    {"id": 27, "name": "Telegram", "url": "core.telegram.org", "category": "Communications and Messaging"},
    {"id": 28, "name": "WhatsApp Business", "url": "developers.facebook.com/docs/whatsapp", "category": "Communications and Messaging"},
    {"id": 29, "name": "Aircall", "url": "aircall.io", "category": "Communications and Messaging"},
    {"id": 30, "name": "Vonage", "url": "developer.vonage.com", "category": "Communications and Messaging"},
    {"id": 31, "name": "Google Ads", "url": "developers.google.com/google-ads", "category": "Marketing Ads Email and Social"},
    {"id": 32, "name": "Meta Ads", "url": "developers.facebook.com/docs/marketing-apis", "category": "Marketing Ads Email and Social"},
    {"id": 33, "name": "LinkedIn Ads", "url": "learn.microsoft.com/linkedin/marketing", "category": "Marketing Ads Email and Social"},
    {"id": 34, "name": "GoHighLevel", "url": "highlevel.stoplight.io", "category": "Marketing Ads Email and Social"},
    {"id": 35, "name": "Mailchimp", "url": "mailchimp.com/developer", "category": "Marketing Ads Email and Social"},
    {"id": 36, "name": "Klaviyo", "url": "developers.klaviyo.com", "category": "Marketing Ads Email and Social"},
    {"id": 37, "name": "Systeme.io", "url": "systeme.io", "category": "Marketing Ads Email and Social"},
    {"id": 38, "name": "Pinterest", "url": "developers.pinterest.com", "category": "Marketing Ads Email and Social"},
    {"id": 39, "name": "Threads", "url": "developers.facebook.com/docs/threads", "category": "Marketing Ads Email and Social"},
    {"id": 40, "name": "SendGrid", "url": "sendgrid.com", "category": "Marketing Ads Email and Social"},
    {"id": 41, "name": "Shopify", "url": "shopify.dev", "category": "Ecommerce"},
    {"id": 42, "name": "WooCommerce", "url": "woocommerce.com/document/woocommerce-rest-api", "category": "Ecommerce"},
    {"id": 43, "name": "BigCommerce", "url": "developer.bigcommerce.com", "category": "Ecommerce"},
    {"id": 44, "name": "Salesforce Commerce Cloud", "url": "developer.salesforce.com/docs/commerce", "category": "Ecommerce"},
    {"id": 45, "name": "Magento", "url": "developer.adobe.com/commerce", "category": "Ecommerce"},
    {"id": 46, "name": "Squarespace", "url": "developers.squarespace.com", "category": "Ecommerce"},
    {"id": 47, "name": "Ecwid", "url": "api-docs.ecwid.com", "category": "Ecommerce"},
    {"id": 48, "name": "Gumroad", "url": "gumroad.com/api", "category": "Ecommerce"},
    {"id": 49, "name": "Amazon Selling Partner", "url": "developer-docs.amazon.com/sp-api", "category": "Ecommerce"},
    {"id": 50, "name": "Fanbasis", "url": "fanbasis.com", "category": "Ecommerce"},
    {"id": 51, "name": "DataForSEO", "url": "docs.dataforseo.com", "category": "Data SEO and Scraping"},
    {"id": 52, "name": "SE Ranking", "url": "seranking.com/api", "category": "Data SEO and Scraping"},
    {"id": 53, "name": "Ahrefs", "url": "ahrefs.com/api", "category": "Data SEO and Scraping"},
    {"id": 54, "name": "MrScraper", "url": "docs.mrscraper.com", "category": "Data SEO and Scraping"},
    {"id": 55, "name": "Apify", "url": "docs.apify.com", "category": "Data SEO and Scraping"},
    {"id": 56, "name": "Firecrawl", "url": "firecrawl.dev", "category": "Data SEO and Scraping"},
    {"id": 57, "name": "Bright Data", "url": "brightdata.com", "category": "Data SEO and Scraping"},
    {"id": 58, "name": "Sherlock", "url": "github.com/sherlock-project/sherlock", "category": "Data SEO and Scraping"},
    {"id": 59, "name": "Waterfall.io", "url": "waterfall.io", "category": "Data SEO and Scraping"},
    {"id": 60, "name": "Clay", "url": "clay.com", "category": "Data SEO and Scraping"},
    {"id": 61, "name": "GitHub", "url": "docs.github.com/rest", "category": "Developer Infra and Data"},
    {"id": 62, "name": "Vercel", "url": "vercel.com/docs/rest-api", "category": "Developer Infra and Data"},
    {"id": 63, "name": "Netlify", "url": "docs.netlify.com/api", "category": "Developer Infra and Data"},
    {"id": 64, "name": "Cloudflare", "url": "developers.cloudflare.com/api", "category": "Developer Infra and Data"},
    {"id": 65, "name": "Supabase", "url": "supabase.com/docs", "category": "Developer Infra and Data"},
    {"id": 66, "name": "Neo4j", "url": "neo4j.com/docs/api", "category": "Developer Infra and Data"},
    {"id": 67, "name": "Snowflake", "url": "docs.snowflake.com", "category": "Developer Infra and Data"},
    {"id": 68, "name": "MongoDB Atlas", "url": "mongodb.com/docs/atlas/api", "category": "Developer Infra and Data"},
    {"id": 69, "name": "Datadog", "url": "docs.datadoghq.com/api", "category": "Developer Infra and Data"},
    {"id": 70, "name": "Sentry", "url": "docs.sentry.io/api", "category": "Developer Infra and Data"},
    {"id": 71, "name": "Notion", "url": "developers.notion.com", "category": "Productivity and Project Management"},
    {"id": 72, "name": "Airtable", "url": "airtable.com/developers", "category": "Productivity and Project Management"},
    {"id": 73, "name": "Linear", "url": "developers.linear.app", "category": "Productivity and Project Management"},
    {"id": 74, "name": "Jira", "url": "developer.atlassian.com", "category": "Productivity and Project Management"},
    {"id": 75, "name": "Asana", "url": "developers.asana.com", "category": "Productivity and Project Management"},
    {"id": 76, "name": "Monday.com", "url": "developer.monday.com", "category": "Productivity and Project Management"},
    {"id": 77, "name": "ClickUp", "url": "clickup.com/api", "category": "Productivity and Project Management"},
    {"id": 78, "name": "Coda", "url": "coda.io/developers", "category": "Productivity and Project Management"},
    {"id": 79, "name": "Smartsheet", "url": "smartsheet.com/developers", "category": "Productivity and Project Management"},
    {"id": 80, "name": "Harvest", "url": "harvestapp.com", "category": "Productivity and Project Management"},
    {"id": 81, "name": "Stripe", "url": "stripe.com/docs/api", "category": "Finance and Fintech"},
    {"id": 82, "name": "Plaid", "url": "plaid.com/docs", "category": "Finance and Fintech"},
    {"id": 83, "name": "Binance", "url": "binance-docs.github.io", "category": "Finance and Fintech"},
    {"id": 84, "name": "Paygent Connect", "url": "paygent.com", "category": "Finance and Fintech"},
    {"id": 85, "name": "iPayX", "url": "ipayx.ai/docs", "category": "Finance and Fintech"},
    {"id": 86, "name": "QuickBooks", "url": "developer.intuit.com", "category": "Finance and Fintech"},
    {"id": 87, "name": "Xero", "url": "developer.xero.com", "category": "Finance and Fintech"},
    {"id": 88, "name": "Brex", "url": "developer.brex.com", "category": "Finance and Fintech"},
    {"id": 89, "name": "Ramp", "url": "docs.ramp.com", "category": "Finance and Fintech"},
    {"id": 90, "name": "PitchBook", "url": "pitchbook.com", "category": "Finance and Fintech"},
    {"id": 91, "name": "NotebookLM", "url": "cloud.google.com/gemini", "category": "AI Research and Media"},
    {"id": 92, "name": "Otter AI", "url": "help.otter.ai", "category": "AI Research and Media"},
    {"id": 93, "name": "Fathom", "url": "fathom.video", "category": "AI Research and Media"},
    {"id": 94, "name": "Consensus", "url": "consensus.app", "category": "AI Research and Media"},
    {"id": 95, "name": "Reducto", "url": "reducto.ai/docs", "category": "AI Research and Media"},
    {"id": 96, "name": "Devin", "url": "docs.devin.ai", "category": "AI Research and Media"},
    {"id": 97, "name": "Higgsfield", "url": "higgsfield.ai/cli", "category": "AI Research and Media"},
    {"id": 98, "name": "Mermaid CLI", "url": "github.com/mermaid-js/mermaid-cli", "category": "AI Research and Media"},
    {"id": 99, "name": "YouTube Transcript", "url": "transcriptapi.com", "category": "AI Research and Media"},
    {"id": 100, "name": "Grain", "url": "grain.com", "category": "AI Research and Media"},
]

def research_app(app):
    prompt = f"""Research {app['name']} ({app['url']}) and return ONLY this JSON, no extra text:
{{"id":{app['id']},"name":"{app['name']}","category":"{app['category']}","what_it_does":"one line","auth_methods":"OAuth2/API Key/Basic/Token/Other","self_serve_vs_gated":"Self-serve or Gated + why","api_surface":"REST/GraphQL/None + breadth","mcp_available":"Yes/No/Unknown","buildability_verdict":"Ready/Needs outreach/Not buildable + blocker","evidence_url":"{app['url']}","notes":"caveat or none"}}"""

    for attempt in range(3):
        try:
            response = groq_client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[{"role": "user", "content": prompt}],
                temperature=0.1,
                max_tokens=300
            )
            text = response.choices[0].message.content.strip()
            if "```" in text:
                text = text.split("```")[1]
                if text.startswith("json"):
                    text = text[4:]
                text = text.strip().rstrip("```")
            result = json.loads(text)
            print(f"OK {app['id']}/100 -- {app['name']}")
            return result
        except Exception as e:
            err = str(e)
            if "429" in err:
                wait = 30 * (attempt + 1)
                print(f"Rate limited on {app['name']}, waiting {wait}s...")
                time.sleep(wait)
            else:
                print(f"ERROR {app['id']}/100 -- {app['name']} -- {err[:80]}")
                break

    return {
        "id": app['id'],
        "name": app['name'],
        "category": app['category'],
        "what_it_does": "Research failed",
        "auth_methods": "Unknown",
        "self_serve_vs_gated": "Unknown",
        "api_surface": "Unknown",
        "mcp_available": "Unknown",
        "buildability_verdict": "Unknown",
        "evidence_url": app['url'],
        "notes": "Error after 3 attempts"
    }

def main():
    print("Composio + Groq Research Agent")
    print("=" * 40)
    print(f"Researching {len(research_apps)} apps...\n")

    results = []
    for app in research_apps:
        result = research_app(app)
        results.append(result)
        time.sleep(3)

    with open("results.json", "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2)
    print("\nSaved results.json")

    if results:
        keys = results[0].keys()
        with open("results.csv", "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=keys)
            writer.writeheader()
            writer.writerows(results)
    print("Saved results.csv")
    print("\nDone!")

if __name__ == "__main__":
    main()