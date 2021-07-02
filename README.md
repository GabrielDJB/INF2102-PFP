# INF2102-PFP
Repository for class INF2102 - Final Programming Project, as a part of the Master's program in Informatics at PUC-Rio.


## Project Description

This respository contains the documentation and source code for a coversational tool for capturing developers' design rationale through conversations during the development process. Different users can access different views through _magic links_. Each view comprises a user in a given chat, so 4 users in a single chat would result in 4 different _magic links_.

A more detailed documentation can be found on the file `INF2102 - Relatório PFP - Gabriel D J Barbosa - 2020951.pdf`


## Program Structure

This project is split into a front-end and a back-end, with the source code for each part being located in a different folder.
In terms of the front-end aspect, we have two major mechanisms.
* Webserver (*Node.js*)
* Component-based front-end (*React.js*)

In terms of the back-end aspect, we have two componennts, as well.
* Non-relational database (*MongoDB*)
* Service-based architecture (*Flask*)

Further documentation on each of these parts is available in their folders. There you can find information as to how install each part and activate them to enable the web application. Once all requirements are installed, this can be done via the _deploy.bat_ files.


## Program Interactions

This application basically provides a chat service where each user can send and read messages, tagged according to a pre-determined categorization. Users can select categories from the side menu or via a selector next to the text input, attributing the chosen category to the next message sent. This results in a structured collection of documents, each relating a given message.

![image](https://user-images.githubusercontent.com/18614926/124202768-7f048000-dab1-11eb-821f-4afa7738df53.png)
