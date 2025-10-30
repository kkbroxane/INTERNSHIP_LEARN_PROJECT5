# PROJECT SUMMARY

### Due date: Next Wednesday

- create an ai chatbot specialized in real estate search
- should be able to fetch from a database to answer user queries
- if queries doesn't exist in db, make suggestions like 'look for a partner' 'find'


### Tasks ======================

- make a timeline
- define database
- find bootstrap templates
- start

---

- upload to database section
- chatbot section

### ============================

ollama pulll llama3.2:latest

# Install Ollama
curl -fsSL https://ollama.com/install.sh | sh

# Pull a Llama3 model
ollama pull llama3

# Test generation
ollama run llama3


curl -V

If that fails, install curl:

sudo apt update && sudo apt install curl -y

2. Download and run the installer manually

Instead of piping directly, let’s save the script first:

curl -fsSL https://ollama.com/install.sh -o install_ollama.sh

chmod +x install_ollama.sh
./install_ollama.sh


bash install_ollama.sh

***
3. Verify installation

Once it finishes, test Ollama:

ollama --version

If it prints a version, it’s installed.

Then pull Llama 3:

ollama pull llama3

And run:

ollama run llama3

***

Step 1: Remove Snap’s curl

We’ll uninstall the sandboxed one and replace it with the native APT version.

sudo snap remove curl

⚙️ Step 2: Install the native curl

Then install the proper system version:

sudo apt update
sudo apt install curl -y

You can confirm you’re using the right one:

which curl

✅ It should say:

/usr/bin/curl

(not /snap/bin/curl)
🚀 Step 3: Install Ollama again

Now re-run the installer cleanly:

curl -fsSL https://ollama.com/install.sh -o install_ollama.sh
bash install_ollama.sh

🧠 Step 4: Verify

Once installed:

ollama --version
ollama pull llama3
ollama run llama3

### ============================

```python
def detect_property_type(user_query):
    q = user_query.lower()
    if "maison" in q:
        return "maison"
    elif "appartement" in q:
        return "appartement"
    elif "terrain" in q:
        return "terrain"
    return None


def search_properties(user_query, top_k=5):
    query_embedding = embed_content(user_query)
    detected_type = detect_property_type(user_query)

    qs = Property.objects.exclude(embedding=None)
    if detected_type:
        qs = qs.filter(type__iexact=detected_type)

    return qs.order_by(CosineDistance("embedding", query_embedding))[:top_k]
```

```python
def send_message(request):
    if request.method == 'POST':

        user_message = request.POST.get('user_message')

        if any(word in user_message.lower() for word in PROPERTY_KEYWORDS):
            top_properties = search_properties(user_message, top_k=3)

            if top_properties:
                properties_text = "\n\n".join(
                    p.get_child_instance().type_info() for p in top_properties
                )

                prompt = (
                    f"L'utilisateur a dit: '{user_message}'.\n"
                    f"Voici les propriétés correspondantes:\n{properties_text}\n"
                    "Réponds de manière naturelle et concise, en te basant sur ces propriétés."
                )
                bot_response = generate_content(prompt)
            else:
                bot_response = "Je n’ai trouvé aucune propriété correspondant à ta recherche."

        else:
            bot_response = generate_content(user_message)

        ChatMessage.objects.create(user_message=user_message, bot_response=bot_response)    
    return redirect('list_messages')

```