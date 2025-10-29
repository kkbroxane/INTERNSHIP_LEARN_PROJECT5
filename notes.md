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