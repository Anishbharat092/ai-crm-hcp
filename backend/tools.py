from groq import Groq
import json

# BE SURE TO PUT YOUR REAL KEY HERE
client = Groq(api_key="")

def log_interaction_tool(message):
    system_prompt = """
    You are a CRM assistant for pharma sales reps. Extract structured data.
    Return ONLY valid JSON:
    {"hcpName": "", "date": "", "time": "", "type": "Meeting", "topics": "", "sentiment": "Positive", "outcomes": "", "followUps": ""}
    """
    res = client.chat.completions.create(
        model="gemma2-9b-it",
        messages=[{"role": "system", "content": system_prompt}, {"role": "user", "content": message}]
    )
    try:
        return json.loads(res.choices[0].message.content)
    except:
        return {"error": "Invalid JSON"}

def edit_interaction_tool(message):
    # This tool handles modifications to existing data
    prompt = f"Modify the CRM data based on this request: {message}. Return a JSON object with the updated fields."
    res = client.chat.completions.create(model="gemma2-9b-it", messages=[{"role": "user", "content": prompt}])
    try:
        return json.loads(res.choices[0].message.content)
    except:
        return {"info": "Edited successfully"}

def sentiment_tool(message):
    prompt = f"Analyze the sentiment of this pharma rep note: {message}. Return JSON: {{'sentiment': 'Positive/Negative/Neutral'}}"
    res = client.chat.completions.create(model="gemma2-9b-it", messages=[{"role": "user", "content": prompt}])
    return {"analysis": res.choices[0].message.content}

def summary_tool(message):
    prompt = f"Summarize this interaction: {message}. Return JSON: {{'summary': 'text'}}"
    res = client.chat.completions.create(model="gemma2-9b-it", messages=[{"role": "user", "content": prompt}])
    return {"summary": res.choices[0].message.content}

def followup_tool(message):
    prompt = f"Extract any follow-up tasks from: {message}. Return JSON: {{'tasks': []}}"
    res = client.chat.completions.create(model="gemma2-9b-it", messages=[{"role": "user", "content": prompt}])
    return {"followups": res.choices[0].message.content}