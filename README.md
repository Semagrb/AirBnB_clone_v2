# 🌸 HBNB - The Console 🌸

This repository sparkles with the beginnings of a student project, a charming endeavor to create a magical clone of the AirBnB website. Our journey starts with the creation of a backend interface, a console, to manage the enchanting world of program data. With the console commands, users can effortlessly create, update, and destroy objects, all while managing the mystical realm of file storage. Thanks to the magic of JSON serialization/deserialization, the storage is persistent, ensuring the magic lingers between sessions.

---

<center><h3>Repository Contents by Project Task</h3></center>

| Tasks | Description |
| ----- | ------ |
| 0: Authors/README File | Project authors |
| 1: Pep8 | All code is pep8 compliant |
| 2: Unit Testing | All class-defining modules are unittested |
| 3. Make BaseModel | Defines a parent class to be inherited by all model classes |
| 4. Update BaseModel w/ kwargs | Adds functionality to recreate an instance from a dictionary representation |
| 5. Create FileStorage class | Defines a class to manage a persistent file storage system |
| 6. Console 0.0.1 | Adds basic functionality to the console program, allowing it to quit, handle empty lines, and ^D |
| 7. Console 0.1 | Updates the console with methods allowing the user to create, destroy, show, and update stored data |
| 8. Create User class | Dynamically implements a user class |
| 9. More Classes | Dynamically implements more classes |
| 10. Console 1.0 | Updates the console and file storage system to work dynamically with all classes and updates file storage |

<br>
<br>
<center> <h2>General Use</h2> </center>

1. First, clone this repository.

3. Once the repository is cloned, locate the "console.py" file and run it as follows:

/AirBnB_clone$ ./console.py

4. When this command is run, the following prompt should appear:

(hbnb)

5. This prompt designates you are in the "HBnB" console. There are a variety of commands available within the console program.

##### Commands
 * create - Creates an instance based on the given class
 * destroy - Destroys an object based on class and UUID
 * show - Shows an object based on class and UUID
 * all - Shows all objects the program has access to, or all objects of a given class
 * update - Updates existing attributes an object based on class name and UUID
 * quit - Exits the program (EOF will as well)

##### Alternative Syntax
Users can issue a number of console commands using an alternative syntax:

 Usage: <class_name>.<command>([<id>[name_arg value_arg]|[kwargs]])
Advanced syntax is implemented for the following commands: 

 * all - Shows all objects the program has access to, or all objects of a given class
 * count - Returns the number of object instances by class
 * show - Shows an object based on class and UUID
 * destroy - Destroys an object based on class and UUID
 * update - Updates existing attributes an object based on class name and UUID

<br>
<br>
<center> <h2>Examples</h2> </center>
<h3>Primary Command Syntax</h3>

###### Example 0: Create an object
Usage: create <class_name>


