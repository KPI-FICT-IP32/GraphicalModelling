void base_shape_2(float cx, float cy, float w, float h) {
  float x1 = cx - w/2;
  float y1 = cy - h/2;

  float x2 = cx + w/2;
  float y2 = cy + h/2;
  
  beginShape();
   vertex(x1, y1);
   vertex(x2, y1);
   vertex(x1, y2);
   vertex(x2, y2);
   vertex(x1, y1);  
  endShape();
}

void compose(int count, float w1, float h1, float wn, float hn, float rot, float koef) {
  float dw = (wn - w1) / count;
  float dh = (hn - h1) / count;
  
  for(int i = 0; i < count; i++) {
    float w = w1 + dw * i;
    float h = h1 + dh * i;
    
    float posx = (w + max(w1, wn)) / 2;
    pushMatrix();
      translate(posx * koef * i, 0);
      rotate(rot*i);
      base_shape_2(0, 0, w, h);
    popMatrix();    
  }
}

void pattern(int cnt, int cnt_l, int w1, int h1, int wn, int hn, float angle, float dist_koef, int scale_koef, boolean rotate) {
 background(0, 50, 100);
 translate(width*0.5, height*0.5);
 if (scale_koef > 1) {
   scale((frameCount % scale_koef) / (1.0 * scale_koef));
 }
 if (rotate) {
   rotate(frameCount / 200.0);
 }
 
 for (int i = 0; i < cnt; ++i) {
   float rot = 2*PI / cnt;
   pushMatrix();
     rotate(i * rot);
     compose(cnt_l, w1, h1, wn, hn, angle, dist_koef);
   popMatrix();
 }
}

void setup() {
  size(768, 768);
  stroke(255, 255, 0);
  fill(0, 50, 100);
}

void draw() {
  pattern(12, 10, 40, 40, 0, 0, PI/4, 0.9, 10, true);
}
