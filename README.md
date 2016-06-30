# Gordon
Gordon is an collection of autotests for [Crowbar](https://github.com/crowbar/crowbar). Currently it's in the POC stage and it's working only with SOC6 which is the last version of SUSE Openstack Cloud. 

SUSE uses Crowbar in Cloud and Storage products and it takes some time to test each element of it's web interface (also, we need to do it twice - before and after each update) so it's really helpful for testers to have a collection of autotests for that. 

There's a short demonstration about gordon in action
![Animation](https://raw.githubusercontent.com/Evalle/gordon/master/desktop-animation.gif "Gordon in action")

and also video [![gordon](https://asciinema.org/a/3rov78z1vns1n5a7jpn37n55s.png)](https://asciinema.org/a/3rov78z1vns1n5a7jpn37n55s)


This project is written in Python and uses [Splinter library](https://splinter.readthedocs.io/en/latest/)

p.s. the name of the project was inspired by [Gordon Freeman] (https://en.wikipedia.org/wiki/Gordon_Freeman) because who knows better how to deal with crowbar :) ? 
<p align="center">
  <img src="https://raw.githubusercontent.com/Evalle/gordon/master/gordon.jpg?raw=true" alt="Gordon image"/>
</p>

##Preparations

1) First of all you'll need a couple of additional libraries. Each of them can be installed via **pip** https://pypi.python.org/pypi/pip

```
$ pip install selenium splinter
```
It’s important to note that you also need to have Google Chrome installed in your machine.

2) Then you need to clone current repository 
``` 
$ git clone https://github.com/Evalle/gordon.git
```

3) Now you can run **gordon** (see Examples section).

## Arguments

- **`nodes`:**  amoount of nodes, for example: **'4'** , **'12'**
- **`address`:**  crowbar ip addresss for example: **'192.168.0.123'**
- **`port`:** crowbar port, for example: **'80'** , **'3000'**
- **`--help, -h`:**  help message.

## Examples

```
$ gordon 4 192.168.0.2 8080

Main page tests
===============

By text
*******
4 nodes                                                      PASSED
crowbar                                                      PASSED
dashboard                                                    PASSED

--- cut --- 
```

```
$ gordon -h
usage: gordon [-h] nodes address port

Crowbar auto testsuite, run it via 'gordon -a <address> -p <port>'

positional arguments:
  nodes       amount of nodes, for example 4
  address     crowbar address, for example 192.168.0.2
  port        crowbar port, for example 80, 3000

optional arguments:
  -h, --help  show this help message and exit

```

### Free software

gordon - Copyright (C) 2016 Evgeny Shmarnev shmarnev@gmail.com

gordon is a free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

gordon is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
