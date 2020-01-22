import time
from concurrent import futures
from typing import List

import grpc

import tokenization_pb2
import tokenization_pb2_grpc
import tokenizer


def token_to_detail_response(token: List[List[str]]) -> tokenization_pb2.TokenDetail:
    reading = "*"
    pronounce = "*"
    if len(token[1]) > 8:
        reading = token[1][7]
        pronounce = token[1][8]
    return tokenization_pb2.TokenDetail(
        surface=token[0],
        pos=token[1][0],
        pos_detail_1=token[1][1],
        pos_detail_2=token[1][2],
        pos_detail_3=token[1][3],
        toc=token[1][4],
        conjugation=token[1][5],
        original_form=token[1][6],
        reading=str(reading),
        pronounce=str(pronounce),
    )


class TokenizerStreamServicer(tokenization_pb2_grpc.TokenizerStreamServicer):
    def __init__(self):
        pass

    def TokenizerStreamServer(self, request_iterator, context):
        t = tokenizer.TokenizationService()
        for new_msg in request_iterator:
            reply_msgs = []
            tokens = t.tokenize(new_msg.text)
            reply_msgs.append(tokenization_pb2.TokenizeResponse(tokens=tokens))
            for message in reply_msgs:
                yield message


class TokenizerServicer(tokenization_pb2_grpc.TokenizerServicer):
    def __init__(self):
        pass

    def TokenizerServer(self, request, context):
        t = tokenizer.TokenizationService()
        pos_filter = request.pos_filter
        tokens = t.tokenize(request.text)
        return tokenization_pb2.TokenizeResponse(tokens=tokens)


class TokenizerDetailStreamServicer(
    tokenization_pb2_grpc.TokenizerDetailStreamServicer
):
    def __init__(self):
        pass

    def TokenizerDetailStreamServer(self, request_iterator, context):
        t = tokenizer.TokenizationService()
        for new_msg in request_iterator:
            reply_msgs = []
            pofs = new_msg.pos_filter
            tokens = []
            if len(pofs) > 0:
                tokens = t.tokenize(new_msg.text, detail=True, pofs=pofs)
            else:
                tokens = t.tokenize(new_msg.text, detail=True)
            token_details = []
            for token in tokens:
                token_details.append(token_to_detail_response(token))

            reply_msgs.append(
                tokenization_pb2.TokenizeDetailResponse(tokens=token_details)
            )
            for message in reply_msgs:
                yield message


class TokenizerDetailServicer(tokenization_pb2_grpc.TokenizerDetailServicer):
    def __init__(self):
        pass

    def TokenizerDetailServer(self, request, context):
        t = tokenizer.TokenizationService()
        pofs = request.pos_filter
        tokens = []
        if len(pofs) > 0:
            tokens = t.tokenize(request.text, detail=True, pofs=pofs)
        else:
            tokens = t.tokenize(request.text, detail=True)

        token_details = []
        for token in tokens:
            token_details.append(token_to_detail_response(token))

        return tokenization_pb2.TokenizeDetailResponse(tokens=token_details)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

    tokenization_pb2_grpc.add_TokenizerServicer_to_server(TokenizerServicer(), server)
    tokenization_pb2_grpc.add_TokenizerStreamServicer_to_server(
        TokenizerStreamServicer(), server
    )

    tokenization_pb2_grpc.add_TokenizerDetailServicer_to_server(
        TokenizerDetailServicer(), server
    )
    tokenization_pb2_grpc.add_TokenizerDetailStreamServicer_to_server(
        TokenizerDetailStreamServicer(), server
    )

    server.add_insecure_port("[::]:6565")
    server.start()
    try:
        while True:
            time.sleep(3)
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == "__main__":
    serve()
