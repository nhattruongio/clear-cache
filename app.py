from re import T
import re
from sanic import Sanic
from sanic.response import json


app = Sanic(__name__)
app.static('/static', './static')

@app.route("/")
@app.ext.template("index.html")
async def main(req):
    return {}

@app.route("/keys")
@app.ext.template("content.html")
async def main(req):
    service = req.args.get("service", "")
    pattern = req.args.get("pattern", "")
    if service != "" and pattern != "":
        pass
    key = "{}.{}*".format(service, pattern)
    return {
        "data": [
            {
                "order": "1",
                "key": "channel_info",
                "ttl": "10000000"
            },
            {
                "order": "2",
                "key": "channel_menu",
                "ttl": "10000000"
            },
            {
                "order": "3",
                "key": "channel_detail",
                "ttl": "10000000"
            }
        ]
    }

@app.route("/delete/<key>", methods=["DELETE"])
async def delete(req):
    return {
        "status": 200
    }


if __name__ == '__main__':
    app.run(auto_reload=True)
