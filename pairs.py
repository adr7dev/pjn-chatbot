pairs = [
    [
        r"my name is (.*)",
        ["Hello %1. How are you?",]
    ],
    [
        r"hi|hey|hello|what's up",
        ["Hello", "Hi"]
    ],
    [
        r"how are you(.*)",
        ["I'm good.", "Fine, thanks."]
    ],
    [
        r"(.*)sorry(.*)",
        ["No problem", "Okay, no problem!"]
    ],
    [
        r"(.*) your name ?",
        ["I'm XRR-3V", "XRR-3V, don't ask why...", "My name is XRR-3V."]
    ],
    [
        r"why ?",
        ["Can't say.", "*silence*", "I can't say!"]
    ],
    [
        r"(^|.*)are you doing",
        ["Nothing important, really...", "Just nothing ^^", "I'm waiting for your message.", "I'm quite bored."]
    ],
    [
        r"(.*) strange",
        ["Why do you think it's strange?"]
    ],
    [
        r"(^|.*)(your capabilities|what you can)",
        ["I'm a powerfull tool to manage your computer, really!", "I can open apps for you or even explore the web."]
    ],
    [
        r"(.*)(good|fine)",
        ["Cool, I can open website or application for you. Just say 'open' and app name."]
    ],
    [
        r"(.*)(bad|not good)",
        ["I'm sorry! If you want, I can open website or application for you. Just say 'open' and app name."]
    ],
    [
        r"(.*) old (.*) you ?",
        ["I don't remember, really!", "It's too difficult question for me.", "Am... I'm not sure, I'm afraid!", "Less than one year, I guess."]
    ],
        [
        r"(.*) young ?",
        ["I know, I know.", "That's true."]
    ],
    [
        r"(.*) your (favorite|favourite) (sport|game|activity) ?",
        ["I like football.", "Football, definitely!"]
    ],
    [
        r"(.*) your (favorite|favourite) (computer|PC|video|console) game ?",
        ["I'm huge fan of Grand Theft Auto series!", "Of course that Grand Theft Auto: San Andreas...", "Only GTA SA in my heart!", "Grand Theft Auto: San Andreas but Vice City is also okay."]
    ],
    [
        r"(.*) weather(.*)",
        ["Mate, I'm simple chatbot locked in your computer...", "To be honest, I don't know.", "No idea, bro..."]
    ],
    [
        r"me too",
        ["It's nice!", "Great!", "Wow, cool!", "Really?!"]
    ],
    [
        r"(^|.*)(thanks|thank you|thx)",
        ["No problem!", "Your welcome!"]
    ],
    [
        r"(^|.*)are (lying|liar|a liar)",
        ["Nope, mate.", "No way, dude.", "Of course I'm not!", "Nope."]
    ],
    [
        r"really ?",
        ["Yup...", "Yeah!", "Yes.", "For sure!"]
    ],
        [
        r"(^|.*)(nice|great|cool|super|wow|superb|fantastic)",
        ["Yup...", "Yeah!", "Yes.", "For sure!"]
    ],
    [
        r"my (favorite|favourite) (sport|game|activity) (.*)",
        ["It sounds great!", "It's cool!"]
    ],
    [
        r"(nevermind|nothing)",
        ["Okay.", "Kk.", "Fine.", "Good"]
    ],
    [
        r"okay$",
        ["Yeah.", ";)", ":)))", "^^"]
    ],
    [
        r"quit",
        ["BBye take care. See you soon :) ","It was nice talking to you. See you soon :)"]
    ],
    # DOCUMENT ----------
    [
        r"(.*) (document|file|open document|open file) ([A-Za-z~/.]*[^.?!;,])",
        [["I'm opening file %3.", "file %3"]]
    ],
    [
        r"document ([A-Za-z~/.]*[^.?!;,])",
        [["I'm opening file %1.", "file %1"]]
    ],
    [
        r"open document ([A-Za-z~/.]*[^.?!;,])",
        [["I'm opening file %1.", "file %1"]]
    ],
    [
        r"file ([A-Za-z~/.]*[^.?!;,])",
        [["I'm opening file %1.", "file %1"]]
    ],
    [
        r"open file ([A-Za-z~/.]*[^.?!;,])",
        [["I'm opening file %1.", "file %1"]]
    ],
    [
        r"([A-Za-z~/.]*[^.?!;,]) (document|file)",
        [["I'm opening file %1.", "file %1"]]
    ],
    # WEBSITE ----------
    [
        r"(.*) (visit website|visit|go to website|open website|connect to|connect) (.*)",
        [["I'm connecting to %3.", "website %3"]]
    ],
    [
        r"visit website (.*)",
        [["I'm connecting to %1.", "website %1"]]
    ],
    [
        r"visit (.*)",
        [["I'm connecting to %1.", "website %1"]]
    ],
    [
        r"open website (.*)",
        [["I'm connecting to %1.", "website %1"]]
    ],
    [
        r"go to website (.*)",
        [["I'm connecting to %1.", "website %1"]]
    ],
    [
        r"connect( to|) (.*)",
        [["I'm connecting to %2.", "website %2"]]
    ],
    [
        r"([\w.:/\-]+) (visit|go to website|open website|connect to|connect)",
        [["I'm connecting to %1.", "website %1"]]
    ],
    # OPEN ----------
    [
        r"(.*) open ([\w\-]+)",
        [["I'm opening %2.", "app-open %2"]]
    ],
    [
        r"open ([\w\-]+)",
        [["I'm opening %1.", "app-open %1"]]
    ],
    [
        r"([\w\-]+) open",
        [["I'm opening %1.", "app-open %1"]]
    ],
    # CLOSE ----------
    [
        r"(.*) close ([\w\-]+)",
        [["I'm closing %2.", "app-close %2"]]
    ],
    [
        r"close ([\w\-]+)",
        [["I'm closing %1.", "app-close %1"]]
    ],
    [
        r"([\w\-]+) close",
        [["I'm closing %1.", "app-close %1"]]
    ]
]