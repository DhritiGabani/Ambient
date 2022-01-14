<center>

# Ambient

</center>

A discord music bot to improve concentration and focus during online study sessions.

<br />

## Technologies Used

- Python
- Discord.py

<br />

## 📷 Screenshots

![Bot in Action](https://github.com/DhritiGabani/Ambient/blob/main/images/Screen%20Shot%202022-01-08%20at%204.01.29%20PM.png?raw=true)

![Voice Channel]("images/Screen Shot 2022-01-08 at 4.02.14 PM.png" "Voice Channel")

![Bot Description]("images/Screen Shot 2022-01-08 at 4.20.52 PM.png" "Bot Description")

<br/>

## Set up a local environment

1. Clone the repository

```shell
git clone https://github.com/DhritiGabani/Ambient
```

2. Navigate to the directory

```shell
cd Ambient
```

3. Create a python virtual environment

```shell
# If virtualenv is not installed
pip3 install virtualenv

# Required step to create
virtualenv venv
```

4. Activate the virtual environment

```shell
source venv/bin/activate    # (For Mac/Linux)
venv\Scripts\activate       # (For Windows)
```

5. Install the required dependencies

```shell
pip install -r requirements.txt
```

6. Create an environment variable to store bot's token

```shell
# Create a .env file at the root of the project and replace your bot token with YOUR_BOT_TOKEN
BOT_TOKEN=YOUR_BOT_TOKEN
```

7. Run the bot after adding to the server

```shell
python bot.py
```

## Bot Commands

- [x] Join
- [x] Leave
- [x] Play
- [x] Pause
- [x] Queue
- [x] Resume
- [x] Loop
- [x] Now Playing
- [x] Skip
- [x] Remove


