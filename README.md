Your wedding gift
=================

So… this is why I asked you for your favorite colors, Tuck. I wrote a little
computer program that took these two "seed" colors…

![Tucker](https://raw.githubusercontent.com/mccutchen/tuck-wedding-gift/master/gift/094fb1-color.png)
![Scotti](https://raw.githubusercontent.com/mccutchen/tuck-wedding-gift/master/gift/0c601e-color.png)

… and turned them into these images:

![Tucker](https://raw.githubusercontent.com/mccutchen/tuck-wedding-gift/master/gift/094fb1-small.png)
![Scotti](https://raw.githubusercontent.com/mccutchen/tuck-wedding-gift/master/gift/0c601e-small.png)

Now, I've never gotten them printed on canvas like this before, so I have no
idea how they'll turn out. I hope they look good, though! You'll have to let me
know.

Incidentally, the versions of the images that you see above have been scaled
down. The full sized versions are huge, because I got them printed on such
large canvases. Here's the [full sized blue image][blue] (8mb) and the [full
sized green image][green] (5.7mb), if you want to see them.

Some technical details, if you're interested
--------------------------------------------

Every time you run the program, the output will be different. You give it a
starting color and it picks every subsequent color based on the first one, and
draws a line for each.

(The only slightly tricky part was coming up with a way to make sure that if
you started with blue, the colors would stay blue the whole time, instead of
going from, say, blue to purple to red.)

(Also, this is called "generative" or "algorithmic" art, and it's what got me
into programming to begin with. I've been playing with variations on this
specific theme for a loooong time now. You can see some similar previous work
[here][lines01], [here][lines02], and [here][lines03].)

Most of the work happens [in this file][lines.py], though you can browse all of
the source code [here][repo], if you want.

If y'all have any questions, you know where to find me.

### With all the love in the world,

### *Riiiiiiitch*

[blue]: https://raw.githubusercontent.com/mccutchen/tuck-wedding-gift/master/gift/094fb1.png
[green]: https://raw.githubusercontent.com/mccutchen/tuck-wedding-gift/master/gift/0c601e.png
[lines01]: http://humortree.org/projects/lines01/
[lines02]: http://humortree.org/projects/lines02/
[lines03]: http://humortree.org/projects/lines03/
[lines.py]: https://github.com/mccutchen/tuck-wedding-gift/blob/master/lines.py
[repo]: https://github.com/mccutchen/tuck-wedding-gift/
