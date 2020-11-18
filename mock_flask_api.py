from flask import Flask, Response, stream_with_context
import time
import uuid
import random

APP = Flask(__name__)

@APP.route("/large_request/<int:rowCount>", methods=["GET"])
def get_large_request(rowCount):
    """return N rows of data"""
    def f():
        """" Generator of pseudo data """
        for _i in range(rowCount):
            time.sleep(0.01)
            txid = uuid.uuid4()
            uid = uuid.uuid4()
            amount = round(random.uniform(-1000,1000), 2)
            yield f"('{txid}', '{uid}', '{amount}')\n"
    return Response(stream_with_context(f()))

if __name__ == "__main__":
    APP.run(debug = True)