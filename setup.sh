echo "$0: Creating virtual enviroment..."
python3 -m venv .env

echo "$0: Entering virtual env..."
. .env/bin/activate

echo "$0: Installing wiki dependencies..."
pip install -r requirements.txt

echo "$0: Setup complete \n"
echo "$0: To start the wiki server, run:"
echo "$0: 'source .env/bin/activate'"
echo "$0: 'zensical serve          '"
