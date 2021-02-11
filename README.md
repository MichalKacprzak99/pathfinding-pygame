# Path finding in pygame
![GitHub](https://img.shields.io/github/license/MichalKacprzak99/pathfinding-pygame)
![GitHub top language](https://img.shields.io/github/languages/top/MichalKacprzak99/pathfinding-pygame)
![GitHub last commit](https://img.shields.io/github/last-commit/MichalKacprzak99/pathfinding-pygame)
## Table of Contents

 * [Project Description](#project-description)
 * [Installation](#installation)
 * [Demo](#demo)
 * [Features](#features)
 * [Future](#future)
 
## Project Description

Purpose of this project is to shown  in very simple way how pathfinding 
can be included in games(and any other applications) created by using Python3.
I used pygame to create simple and interactive demonstration of how to use pathfinding.
To pathfinding I used A* search algorithm. If you wanna read more about this algorithm
I propose this [article](https://en.wikipedia.org/wiki/A*_search_algorithm) 
or a more detailed description available on [wikipedia](https://en.wikipedia.org/wiki/A*_search_algorithm).
More detailed description in future will be available on my first Medium article.
## Installation

    $ git clone https://github.com/MichalKacprzak99/pathfinding-pygame.git
    $ cd pathfinding-pygame/
    $ sudo pip install -r requirements.txt
    
## How to use?   

    $ cd src/
    $ python main.py     
    
## Demo
![here](https://media.giphy.com/media/sSFvUIYp4x1PEmq9xQ/giphy.gif)
## Features
* board contains randomized obstacles which cannot be chosen as start/end point of path
* user can choose start/end point of path by pressing left mouse button
* user can deselect a square by pressing right mouse button
* user can generate to board by pressing R on keyboard, 
    it will cancel any previous actions like choosing start square etc.
* path is displayed as gray squares
## Future?
* Make own implementation of algorithms instead of using ready-made solutions.
* Extend project by visualization of pathfinding process.
* Add another popular pathfinding algorithms.
* Add squares with different weights and check how it will affect pathfinding.
