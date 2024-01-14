AIRBnB Clone: The console.
Project between Sammy Kanyingi and Rita Omondi of C_18
First step: Write a command interpreter to manage your AirBnB objects.
This is the first step towards building your first full web application: the AirBnB clone. This first step is very important because you will use what you build during this project with all other following projects: HTML/CSS templating, database storage, API, front-end integration…

Each task is linked and will help you to:

put in place a parent class (called BaseModel) to take care of the initialization, serialization and deserialization of your future instances
create a simple flow of serialization/deserialization: Instance <-> Dictionary <-> JSON string <-> file
create all classes used for AirBnB (User, State, City, Place…) that inherit from BaseModel
create the first abstracted storage engine of the project: File storage.
create all unittests to validate all our classes and storage engine
=======
AirBnB Clone Command Interpreter

This is project is a simplified AirBnb Clone which has a commandline interpreter for managing an dinteracting with various
objects. The application offers features for creating, updating,reading and destroying classes

To start the command line interpreter
1. Clone the repo to your machine
2. Navigate to project directory
3. Run the command interpreter

To use the command line interpreter;
1. Create a new instance: for example create User
2. Show information about an instance: for example show User 1234
3. Update an instance: for example update User 12345 first_name=Alton last_name=ken
4. Delete an instance: for example destroy User 1234
5. Display all instances of a class: for example all User

Examples
1. Create User email="alton.ken@gmail.com" password="qwerty123" first_name="Alton" last_name="ken"
2. Show User 12345
3. Update User 12345 first_name="Sammy"
4. Destroy User 12345
5. All User

