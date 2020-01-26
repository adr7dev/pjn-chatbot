import re
import random
import subprocess
from six.moves import input
from commands import proceedCommand

reflections = {
}

class Chats(object):
    def __init__(self, pairs, reflections={}):

        self._pairs = [(re.compile(x, re.IGNORECASE), y) for (x, y) in pairs]
        self._reflections = reflections
        self._regex = self._compile_reflections()

    def _compile_reflections(self):
        sorted_refl = sorted(self._reflections.keys(), key=len, reverse=True)
        return re.compile(
            r"\b({0})\b".format("|".join(map(re.escape, sorted_refl))), re.IGNORECASE
        )

    def _substitute(self, str):
        return self._regex.sub(
            lambda mo: self._reflections[mo.string[mo.start() : mo.end()]], str.lower()
        )

    def _wildcards(self, response, match):
        pos = response.find('%')
        while pos >= 0:
            num = int(response[pos + 1 : pos + 2])
            response = (
                response[:pos]
                + self._substitute(match.group(num))
                + response[pos + 2 :]
            )
            pos = response.find('%')
        return response

    def respond(self, str):
    # check each pattern
        for (pattern, response) in self._pairs:
            match = pattern.match(str)

            # did the pattern match?
            if match:
                resp = random.choice(response)  # random

                if (isinstance(resp, list)):
                    #print("<debug: command>")
                    final_resp = self._wildcards(resp[0], match)  # wildcard for text response
                    cmd = self._wildcards(resp[1], match)  # wildcard for command execution
                    proceedCommand(cmd)
                    return final_resp
                else:
                    resp = self._wildcards(resp, match)  # wildcard for text response

                    # fix munged punctuation at the end
                    if resp[-2:] == '?.':
                        resp = resp[:-2] + '.'
                    if resp[-2:] == '??':
                        resp = resp[:-2] + '?'
                    return resp

    # Hold a conversation with a chatbot
    def converse(self, quit="quit"):
        user_input = ""
        while user_input != quit:
            user_input = quit
            try:
                user_input = input(">>> ")
            except EOFError:
                print(user_input)
            if user_input:
                while user_input[-1] in "!.":
                    user_input = user_input[:-1]
                print(self.respond(user_input))