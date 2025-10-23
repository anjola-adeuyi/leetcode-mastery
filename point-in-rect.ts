class Point {
  x: number;
  y: number;
}
class Rect {
  topLeft: Point;
  bottomRight: Point;
}

function pointInRect(p: Point, r: Rect): boolean {
  // Validation: handle null/undefined
  if (!p || !r || !r.topLeft || !r.bottomRight) {
    return false;
  }

  // Check if point's coordinates are within rectangle bounds
  return p.x >= r.topLeft.x && p.x <= r.bottomRight.x && p.y >= r.topLeft.y && p.y <= r.bottomRight.y;
}

// Test cases
// Edge case 1: Point exactly on top-left corner
const r1 = pointInRect({ x: 0, y: 0 }, { topLeft: { x: 0, y: 0 }, bottomRight: { x: 5, y: 5 } });
console.log({ r1 });
// Should return: true

// Edge case 2: Point exactly on bottom-right corner
const r2 = pointInRect({ x: 5, y: 5 }, { topLeft: { x: 0, y: 0 }, bottomRight: { x: 5, y: 5 } });
console.log({ r2 });
// Should return: true

// Edge case 3: Point just outside right edge
const r3 = pointInRect({ x: 5.1, y: 3 }, { topLeft: { x: 0, y: 0 }, bottomRight: { x: 5, y: 5 } });
console.log({ r3 });
// Should return: false

// Edge case 4: Zero-area rectangle (line or point)
const r4 = pointInRect({ x: 2, y: 2 }, { topLeft: { x: 2, y: 2 }, bottomRight: { x: 2, y: 2 } });
console.log({ r4 });
// Should return: true (point is exactly on the single point)



// To run
// npx tsx point-in-rect.ts
// deno run point-in-rect.ts
