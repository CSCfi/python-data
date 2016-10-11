---
layout: post
title:  "Introduction to Python Notebook available!"
date:   2016-10-10 10:08:06 +0300
categories: Jupyter notebook intro
---

This is an attempt to see how usable the Pouta Blueprints is for students
without prior exposure to it. If you encounter problems or want to give
feedback about the user experience of either the login process or the content
of the Notebook don't hesitate to contact _jyry.suvilehto_ at the TLD _csc.fi_
. Even negative feedback is welcome!

To access the notebook navigate to [Pouta Blueprints](https://pb.csc.fi/) and
log in using Haka authentication. Pouta Blueprints is a system for
provisioning ephemeral resources in private clouds. Whatever you do inside an
environment is destroyed when the lifetime of the environment is over.

Once logged in, start an instance of the Jupyter Notebook container, you may
have to scroll down to find it

![Jupyter notebook]({{ "/assets/img/instructions/pb_jupyter_notebook.png" | prepend:site.baseurl }})

Wait for a while until you can click the Open in browser link

![Open in browser]({{ "/assets/img/instructions/pb_open_in_browser.png" | prepend:site.baseurl }})

Then start a new terminal 

![New Terminal]({{ "/assets/img/instructions/jupyter_new_terminal.png" | prepend:site.baseurl }})

You should see a web-based terminal like this

![Terminal]({{ "/assets/img/instructions/jupyter_terminal.png" | prepend:site.baseurl }})

Where you should run the command

        wget \
        https://csc-it-center-for-science.github.io/python-data/assets/notebooks/intro.ipynb

n the terminal. Go back to the Jupyter notebook view. You may have to press
the refresh button in the corner.

Finally when you click on the name of the file Jupyter will open the notebook
for you and you can do the tutorial.

![Downloaded File]({{ "/assets/img/instructions/pb_downloaded_file.png" | prepend:site.baseurl }})

In the end you should see this view and be able to access the tutorial.
![Downloaded File]({{ "/assets/img/instructions/jupyter_intro.png" | prepend:site.baseurl }})

**remember everything you do will be wiped out after the container is closed!**
