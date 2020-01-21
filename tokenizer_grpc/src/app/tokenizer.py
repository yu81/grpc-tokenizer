import platform
from typing import List

import MeCab

neologd = " -d /usr/lib/x86_64-linux-gnu/mecab/dic/mecab-ipadic-neologd"
if "Darwin" in platform.system():
    neologd = " -d /usr/local/lib/mecab/dic/mecab-ipadic-neologd"
tagger = MeCab.Tagger(neologd)


class TokenizationService:
    def tokenize(self, text: str, detail=False, pofs=("名詞", "形容詞", "動詞")):
        try:
            if not detail:
                result = [
                    w[0]
                    for w in self.filter_tokens(
                        self.parsed_to_tokens(tagger.parse(self.remove_return(text))),
                        pofs=pofs,
                    )
                ]
                return result
            result = [
                w
                for w in self.filter_tokens(
                    self.parsed_to_tokens(tagger.parse(self.remove_return(text))),
                    pofs=pofs,
                )
            ]
            return result

        except KeyError as e:
            return []
        except ValueError as e:
            return []

    def remove_return(self, text: str) -> str:
        return text.replace("\n", " ")

    def parsed_to_tokens(self, parsed_text: str) -> List[List[str]]:
        lines = parsed_text.rstrip().rstrip("EOS").split("\n")
        result = [line.split("\t") for line in lines if line != ""]
        result = [[r[0], r[1].split(",")] for r in result]
        return result

    def filter_tokens(self, tokens, pofs=("名詞", "形容詞", "動詞")):
        return [token for token in tokens if token[1][0] in pofs]
