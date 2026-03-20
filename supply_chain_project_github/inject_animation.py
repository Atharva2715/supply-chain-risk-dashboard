import os

html_path = 'c:/Users/Atharva/OneDrive/Desktop/supply chain risk/chainguard_demo.html'
with open(html_path, 'r', encoding='utf-8') as f:
    text = f.read()

# Make the Real-Time Location Tracker map interactive by drawing actual animated markers moving along lines, not just jumping
# We can inject advanced Javascript to animate Leaflet markers

js_inject = """
    // --- ADVANCED VEHICLE ANIMATION LOGIC ---
    let animationFrameId;
    let startTime;
    
    function startSmoothAnimations() {
       if(animationFrameId) cancelAnimationFrame(animationFrameId);
       startTime = performance.now();
       
       // Calculate paths
       SHIPMENTS.forEach(s => {
          s.startLat = s.from.lat;
          s.startLng = s.from.lng;
          s.endLat = s.to.lat;
          s.endLng = s.to.lng;
          
          // Random offset so they don't all start linearly
          s.progressBase = Math.random() * 10000;
          
          if(s.status === 'stopped') {
             s.speed = 0;
          } else if(s.status === 'delayed') {
             s.speed = 0.0001; // extremely slow
          } else {
             s.speed = 0.0003 + (Math.random() * 0.0002); // normal speed
          }
       });
       
       function step(timestamp) {
           let elapsed = timestamp - startTime;
           
           routeLines.forEach(item => {
               if(item.isTruckMarker) {
                   const s = item.shipment;
                   if(s.speed > 0) {
                       let p = ((elapsed + s.progressBase) * s.speed) % 2; // goes 0 to 2
                       let percent = p > 1 ? 2 - p : p; // ping pong 0 to 1 to 0
                       
                       // Interpolate position
                       let curLat = s.startLat + (s.endLat - s.startLat) * percent;
                       let curLng = s.startLng + (s.endLng - s.startLng) * percent;
                       
                       item.setLatLng([curLat, curLng]);
                   }
               }
           });
           animationFrameId = requestAnimationFrame(step);
       }
       animationFrameId = requestAnimationFrame(step);
    }
"""

if "// --- ADVANCED VEHICLE ANIMATION LOGIC ---" not in text:
    text = text.replace("    function drawRouteLines() {", js_inject + "\n    function drawRouteLines() {")
    
    # Let's attach metadata to truck markers so we can query them above
    target_marker = "const tMarker = L.marker([midLat, midLng], { icon: truckIcon }).addTo(mapInstance);"
    replace_marker = """const tMarker = L.marker([midLat, midLng], { icon: truckIcon }).addTo(mapInstance);
        tMarker.isTruckMarker = true;
        tMarker.shipment = s;"""
        
    text = text.replace(target_marker, replace_marker)
    
    # Start animation at bottom of drawRouteLines
    text = text.replace("routeLines.push(line, tMarker);\n      });", "routeLines.push(line, tMarker);\n      });\n      startSmoothAnimations();")
    
with open(html_path, 'w', encoding='utf-8') as f:
    f.write(text)

print("Injected smooth map animations!")
