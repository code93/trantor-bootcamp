Co-ordinate X, Y and Z are specific for specific users to allocate their username on the Map 
which can be zoomed in and out and therefore a third coordinate.

Dashboard ID is the key for the Dashoboard editing subpage that allows to edit Features like 
Posts, Portfolio's, etc to be edited and in future versions of this to create features.

Features ID is the key linking all the features like Posts and Portfolio's by their keys.

Post ID is the key for the Posts of a User to be linked by.

Each User has an ID which is the main key to that partiular user to which relationships in Database(or kind)
can be created.


The Tables are as follows:

1. User Table (Primary or Main table)
	1. ID (primary key)
	2. Email
	3. Username
	4. Password

2. Game-Map Table (/* It is called game map as Map might confuse or complicate things later on**/) (linked to User Table)
	1. Co-ordinate ID
	2. Co-ordinate X
	3. Co-ordinate Y
	4. Co-ordinate Z
	

3. Mega Features Table(/* mega is used to not to be confused with features like buttons and kind)
	1. Features ID
	2. Posts
	3. Portfolio

4. Dashboard Table (linked to Mega features table)
	1. Dashboard ID (Since A page will be allocated to user editing and vieweing all the MEga features)
	2. User Dashboard 

5. Posts Table (linked to Mega features table)
	1. Post ID
	2. Post

6. Portfolio Table (linked to Mega features table)
	1. Portfolio ID
	2. Portfolio



   