
# React-Three-Fiber

react-three-fiber is a React renderer for threejs. Build your scene declaratively with re-usable, self-contained components that react to state, are readily interactive and can participate in React's ecosystem.




## Installation

Install react-three-fibre with npm in your project folder

```bash
  npm install three @react-three/fiber
```
    
## Ecosystem

- `@react-three/gltfjsx` – turns GLTFs into JSX components
- `@react-three/drei` – useful helpers for react-three-fiber
- `@react-three/postprocessing` – post-processing effects
- `@react-three/flex` – flexbox for react-three-fiber
- `@react-three/xr` – VR/AR controllers and events
- `@react-three/cannon` – physics based hooks
- `@react-three/a11y` – accessibility tools for react-three-fiber
- `zustand` – state management
- `react-spring` – a spring-physics-based animation library
- `react-use-gesture` – mouse/touch gestures


## Canvas

The `Canvas` object is where you start to define your React Three Fiber Scene.

```javascript
import React from 'react'
import { Canvas } from '@react-three/fiber'

const App = () => (
  <Canvas>
    <pointLight position={[10, 10, 10]} />
    <mesh>
      <sphereGeometry />
      <meshStandardMaterial color="hotpink" />
    </mesh>
  </Canvas>
)
```


## Render Props


| PROP | DESCRIPTION     | DEFAULT                |
| :-------- | :------- | :------------------------- |
| **children** | three.js JSX elements or regular components | |
| **gl** | Props that go into the default renderer, or your own renderer. Also accepts a synchronous callback like `gl={canvas => new Renderer({ canvas })}` | `{}`
| **camera** | Props that go into the default camera, or your own `THREE.Camera` | `{ fov: 75, near: 0.1, far: 1000, position: [0, 0, 5] }`
| **shadows** | Props that go into `gl.shadowMap`, can also be set true for `PCFsoft` | `false`
| **raycaster** | Props that go into the default raycaster | `{}`
| **frameloop** | Render mode: always, demand, never | `always`
| **resize** | Resize config, see react-use-measure's options | `{ scroll: true, debounce: { scroll: 50, resize: 0 } }`
| **orthographic** | Creates an orthographic camera | `false`
| **dpr** | Pixel-ratio, use` window.devicePixelRatio`, or automatic: [min, max] | `[1, 2]`
| **legacy** | Enables THREE.ColorManagement.legacyMode in three r139 or later | `false`
| **linear** | Switch off automatic sRGB encoding and gamma correction | `false`
| **events** | Configuration for the event manager, as a function of state | `import { events } from "@react-three/fiber"`
| **eventSource** | The source where events are being subscribed to, HTMLElement | `React.MutableRefObject<HTMLElement>, gl.domElement.parentNode`
| **eventPrefix** | The event prefix that is cast into canvas pointer x/y events | `offset`
| **flat** | Use `THREE.NoToneMapping` instead of `THREE.ACESFilmicToneMapping` | `false`
| **onCreated** | Callback after the canvas has rendered (but not yet committed) | `(state) => {}`
| **onPointerMissed** | Response for pointer clicks that have missed any target | `(event) => {}`



## Events
`three.js` objects that implement their own `raycast` method (meshes, lines, etc) can be interacted with by declaring events on them. We support pointer events, clicks and wheel-scroll. Events contain the browser event as well as the `three.js` event data (object, point, distance, etc). You may want to polyfill them, if that's a concern.

Additionally, there's a special `onUpdate` that is called every time the object gets fresh props, which is good for things like `self => (self.verticesNeedUpdate = true)`.

Also notice the `onPointerMissed` on the canvas element, which fires on clicks that haven't hit any meshes.

```bash
  <mesh
  onClick={(e) => console.log('click')}
  onContextMenu={(e) => console.log('context menu')}
  onDoubleClick={(e) => console.log('double click')}
  onWheel={(e) => console.log('wheel spins')}
  onPointerUp={(e) => console.log('up')}
  onPointerDown={(e) => console.log('down')}
  onPointerOver={(e) => console.log('over')}
  onPointerOut={(e) => console.log('out')}
  onPointerEnter={(e) => console.log('enter')} // see note 1
  onPointerLeave={(e) => console.log('leave')} // see note 1
  onPointerMove={(e) => console.log('move')}
  onPointerMissed={() => console.log('missed')}
  onUpdate={(self) => console.log('props have been updated')}
/>
```


## Documentation

- [React-Three-Fibre (Canvas)](https://docs.pmnd.rs/react-three-fiber/api/canvas)
- [React-Three-Fibre (Events)](https://docs.pmnd.rs/react-three-fiber/api/events)
