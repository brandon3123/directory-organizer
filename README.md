# Directory Organizer

This is a project that I created to help me organize directorys on my computer. Especially my Downloads folder...

This project contains the following scripts.

1. watchDirectory.py
    * Watches a directory of your choosing and organizes files that are placed inside said directory automatically.
2. directoryHelper.py
    * General script to perform the following on a chosen directory.
        * Count the number of loose files in a directory (ones not inside a folder)
        * Organize the directory. Moves loose files into folders by type/creation date
        * Scans the directory for any unhandled extensions
        
**Note**: I chose to implement custom folder names for a number of extensions. This accomplishes the following.
* More meaningful folder names
* Grouping common extensions together in single folders.

# Instructions

### Watch Directory (Organize dynamically) 

To monitor a directory for changes, open a terminal and simply run the **directoryOrganizer.py** file with a command line argument of the directory to monitor.

    python directoryOrganizer.py /Users/you/Downloads
        
### Run On Mac Startup

1. Create .plist file similar to the following template.

        <?xml version="1.0" encoding="UTF-8"?>
        <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
        <plist version="1.0">
        <dict>
            <key>Label</key>
            <string>directory.organizer.script</string>
            <key>ProgramArguments</key>
            <array>
                <!-- Full path to python 3.x -->
                <string>/usr/local/Cellar/python/3.7.6_1/Frameworks/Python.framework/Versions/3.7/bin/python3.7</string>
                <!-- Full path to directoryOrganizer.py -->
                <string>/directory-organizer/directoryOrganizer.py</string>
                <!-- Full path of directory you wish to organize -->
                <string>/Users/you/Downloads</string>
            </array>
            <key>RunAtLoad</key>
            <true/>
            <key>StandardErrorPath</key>
            <string>/var/log/directory_organizer.error</string>
            <key>KeepAlive</key>
            <true/>
        </dict>
        </plist>
        
2. Set permissions as root for the .plist file you have created.

       sudo chown root /path/to/plistCreate
3. Move the created .plist file to your launch agents directory.

       mv /path/to/plistCreated ~/Library/LaunchAgents/plistCreated
4. Load the .plist created to launchctl.

       sudo launchctl load ~/Library/LaunchAgents/pListCreated
5. Enjoy! Your script should now be running and will continue to run on startup.

### Directory Helper (Statically Organize)

Open a terminal and run the **directoryHelper.py** file with a command line argument of the directory to organize.

    python directoryHelper.py /Users/you/Downloads
    
The following functionality will be available to you.

* Count the number of loose files in a directory (ones not inside a folder)
* Organize the directory. Moves loose files into folders by type/creation date
* Scans the directory for any unhandled extensions