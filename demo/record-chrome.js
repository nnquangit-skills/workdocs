// Hero script for playwright-cli: records the six documentation pages as a video clip for the demo.
//   (cd <workmap repo>/tracking && python3 -m http.server 4606 --bind 127.0.0.1 --directory docs &)   # any workdocs site works
//   playwright-cli open && playwright-cli run-code --filename=demo/record-chrome.js && playwright-cli close
//   ffmpeg -y -i demo/video/public/chrome.webm -c:v libx264 -pix_fmt yuv420p -r 30 -an demo/video/public/chrome.mp4
async (page) => {
  const out = "/Users/nnquangit/projects/private/skills/workdocs/demo/video/public/chrome.webm";
  await page.setViewportSize({ width: 1920, height: 1080 });
  await page.screencast.start({ path: out, size: { width: 1920, height: 1080 }, fps: 30 });
  await page.goto("http://127.0.0.1:4606/index.html");
  await page.waitForTimeout(1500);
  await page.mouse.move(960, 700);
  await page.mouse.wheel(0, 700);
  await page.waitForTimeout(1600);
  await page.goto("http://127.0.0.1:4606/how-it-works.html");
  await page.waitForTimeout(2600);
  await page.mouse.move(960, 700);
  await page.mouse.wheel(0, 760);
  await page.waitForTimeout(5200);
  await page.goto("http://127.0.0.1:4606/demo.html");
  await page.waitForTimeout(900);
  await page.mouse.move(960, 700);
  await page.mouse.wheel(0, 980);
  await page.waitForTimeout(3200);
  await page.goto("http://127.0.0.1:4606/workmap.html");
  await page.waitForTimeout(1800);
  await page.screencast.stop();
}
