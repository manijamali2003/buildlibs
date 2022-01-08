# C++ Project

You can create your open-source c++ project with build-libs script

- Copy example to `packs/`
- Stored your codes in `code`
- Set `compile: Yes` in `manifest`
- Write compile list for your codes
```list
example.cpp:usr/app/example
```
- Write SayeScript for running your compiled code in `/usr/app/`
```saye
run /usr/app/example
```