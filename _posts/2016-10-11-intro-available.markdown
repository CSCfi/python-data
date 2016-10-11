---
layout: post
title:  "Introduction to Python Notebook available!"
date:   2016-10-10 10:08:06 +0300
categories: jekyll update
---

This is an attempt to see how usable the Pouta Blueprints is for students
without prior exposure. If you encounter problems or want to give feedback
about the user experience of either the login process or the content of the
Notebook don't hesitate to contact _jyry.suvilehto_ at the TLD _csc.fi_ . Even
negative feedback is welcome!

To access the notebook navigate to [Pouta Blueprints](https://pb.csc.fi/) and
log in using Haka authentication.

Once logged in, start an instance of the Jupyter Notebook container

![Jupyter notebook]({{ "/assets/img/instructions/pb_jupyter_notebook.png" | prepend:site.baseurl }})

Wait for a while until you can 

![Open in browser]({{ "/assets/img/instructions/pb_open_in_browser.png" | prepend:site.baseurl }})

Then start a new terminal 

![New Terminal]({{ "/assets/img/instructions/jupyter_new_terminal.png" | prepend:site.baseurl }})

And run

        # wget \
        https://csc-it-center-for-science.github.io/python-data/assets/notebooks/intro.ipynb

In the terminal. Go back to the Jupyter notebook view. You may have to press
the refresh button in the corner.

Finally when you click on the name of the file Jupyter will open the notebook
for you.

![Downloaded File]({{ "/assets/img/instructions/pb_downloaded_file.png" | prepend:site.baseurl }})

In the end you should see this view and be able to access the tutorial.
![Downloaded File]({{ "/assets/img/instructions/jupyter_intro.png" | prepend:site.baseurl }})

**remember everything you do will be wiped out after the container is closed!**
