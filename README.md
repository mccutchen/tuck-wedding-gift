Your wedding gift
=================

![Tucker](https://raw.githubusercontent.com/mccutchen/tuck-wedding-gift/master/gift/094fb1-small.png)
![Scotti](https://raw.githubusercontent.com/mccutchen/tuck-wedding-gift/master/gift/0c601e-small.png)

So what in the hell are these two pictures?
-------------------------------------------

Well, first off, I hope they look nice in person. I'm really not sure if they
will, since I've never gotten this kind of image printed on canvas. If they
don't look very good, I'm really sorry about that.

As for what they are: they're images that were created by a computer program I
wrote. Most of the work is done in [lines.py][1], but you can browse all of the
source code above, if you're curious.

Uh, okay.
---------

That's not really a question. Anyway, I've long had a fixation on what's called
"agorithmic" or "generative" art — i.e., art that is created according to a
(generally speaking) simple set of rules. These pictures are an example of that
kind of art. I'll explain the algorithm shortly.

I did this because I thought it would be unique and interesting, and I *hope*
that the final product looks good and that y'all enjoy it.

Tucker, this is why I asked you for your favorite colors. I figured I could
come up with a way to get my computer to make some pretty pictures with those
colors.

All right. What's the algorithm, then?
--------------------------------------

Well, it started with a single shade of blue and a single shade of green. After
playing around with lots of variations, I settled on these two particular
"seed" colors:

![Tucker](https://raw.githubusercontent.com/mccutchen/tuck-wedding-gift/master/gift/094fb1-color.png)
![Scotti](https://raw.githubusercontent.com/mccutchen/tuck-wedding-gift/master/gift/0c601e-color.png)

The algorithm itself is really simple:

 1. Start with a "seed" color
 2. Draw a line
 3. Pick a new color that is close to the first one, but that varies in small
    and random ways
 4. Draw a line
 5. Repeat

The only tricky part was figuring out how to make sure the algorithm kept
generating the same "kind" of color — how to prevent it from migrating from,
e.g., blue to purple to red.

Good god you're boring the hell out of me!
------------------------------------------

I'm sorry about that! I guess that's all I have to offer. For what it's worth,
I picture these being hung on a wall close to each other, so they'd act as a
kind of diptych.

If y'all have any questions, you know where to find me.

### Love,

Riiiiiiitch.

[1]: https://github.com/mccutchen/tuck-wedding-gift/blob/master/lines.py
