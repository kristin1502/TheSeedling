# TheSeedling
__This is a social experiment so check if a group of people can take care of a seedling via twitch.__<br/><br/>
A chatbot filters the commands from all messages in the chat.<br/>
The chatbot determines if a command is valid.<br/>
The valid commands are saved in a MySQL database.<br/>
The RaspberryPi reads the database and executes the first command which is marked as not processed.<br/>
Then either the solenoid valve is activated to water the plant or the servo is being rotated with the sunshade.<br/>
The RaspberryPi also uses a humidity sensor in the potting soil so that nothing is flooded and a light sensor to detect the amount of sunlight on the plant.<br/>
This data of the sensors is then displayed on a website and updated every 30 seconds from the RaspberryPi.<br/>
OBS will display this website on the screen along with some Emojis so you can see the current condition of the plant without knowing much about the plant species.
