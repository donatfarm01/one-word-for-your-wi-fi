# Build notes — One Word for Your Wi-Fi

The bounty asks for one word, between one and twenty characters, that
describes home Wi-Fi as the entrant lives it, and the judge compares
entries two at a time for how funny and how true they are.

The word chosen is diva. The idea came from watching how a home router
actually behaves through a normal day. It is perfectly fine while
nothing important is happening, and it falls apart at exactly the
moment it matters most, a video call, a file upload, the last minutes
of a show. It also only performs in its favourite spot in the house
and needs to be unplugged and plugged back in before it agrees to
work again. That is not a technical fault so much as a temperament,
and temperament is what the word diva names in one short, familiar
word that any reader gets instantly.

Other words were considered and set aside. The obvious ones, slow,
laggy, buffering, dead and spotty, are the words every entrant
reaches for first, so they cannot win on freshness. Moody and
temperamental say the same thing as diva but without the laugh.
Ghosting is funny and true, but it is the kind of clever answer many
entrants will think of, and it reads as a description of a person
rather than of the connection itself. Peekaboo captures the signal
coming and going, but it lands as cute rather than funny. Diva won
because it is the shortest route to the laugh, it stays true to the
daily experience, and it also works as a network name, which is what
the winning word becomes.

The program itself is deliberately tiny. It holds the word as one
constant and writes it to the output file with no trailing newline,
so the file holds exactly four characters. The entry was verified by
running the program locally and reading the output file back, then
checking its length and its hash.

The repository holds the program, a readme with the three make.fun
badges linked to the bounty page, a MIT licence, and these notes.
