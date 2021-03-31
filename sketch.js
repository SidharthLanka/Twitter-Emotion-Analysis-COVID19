let canvas;
const mappa = new Mappa('Leaflet');
const options = {
    lat: 0,
    lng: 0,
    zoom: 1.5,
    style: "http://{s}.tile.osm.org/{z}/{x}/{y}.png"
  }
function preload(){

}
function setup(){
    console.log("sup");
    canvas = createCanvas(800, 600);
    myMap = mappa.tileMap(options)
    myMap.overlay(canvas);
    background(100);
    
}
function draw(){
  clear();
  const nigeria = myMap.latLngToPixel(11.396396, 5.076543); 
  // Using that position, draw an ellipse
  ellipse(nigeria.x, nigeria.y, 20, 20);
}