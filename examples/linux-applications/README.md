# Linux Application Project

- Copy example to `packs/`
- Set `compile: No` in `manifest`
- Copy linux application binary file or AppImage file in `data/usr/app`
- Write SayeScript for running linux binary file in `/usr/app/`
```saye
run /usr/app/example
```