panic(cpu 1 caller 0xfffffff01d7d53dc): x86 CPU CATERR detected
Debugger message: panic
Memory ID: 0xff
OS version: 17P5300
macOS version: 19F101
Kernel version: Darwin Kernel Version 19.5.0: Tue May 26 20:16:42 PDT 2020; root:xnu-6153.121.2~1/RELEASE_ARM64_T8010
Kernel UUID: 123C59BB-125A-31AF-A916-AAF729BE6BE8
iBoot version: iBoot-5540.125.4
secure boot?: YES
x86 EFI Boot State: 0x16
x86 System State: 0x0
x86 Power State: 0x0

shiyebushi.sankuai.com
jdbc:pass=misid;
password:admin do not send to src
后台 代码不泄露
测试数据 啥也不是

kylink
x86 Shutdown Cause: 0xc1
x86 Previous Power Transitions: 0x20002000200
PCIeUp link state: 0x94721614
Paniclog version: 13
Kernel slide:     0x000000001579c000
Kernel text base: 0xfffffff01c7a0000
mach_absolute_time: 0x2149bf02f0a
Epoch Time:        sec       usec
  Boot    : 0x5f4787c4 0x00066161
  Sleep   : 0x5f4dd869 0x000ad888
  Wake    : 0x5f4ddc0d 0x000d302e
  Calendar: 0x5f4dddfa 0x00048cef

Panicked task 0xffffffe000394200: 3300 pages, 216 threads: pid 0: kernel_task
Panicked thread: 0xffffffe0006334d0, backtrace: 0xffffffe015a0b4b0, tid: 344
		  lr: 0xfffffff01d064764  fp: 0xffffffe015a0b4f0
		  lr: 0xfffffff01d0645c0  fp: 0xffffffe015a0b560
		  lr: 0xfffffff01d17f1e0  fp: 0xffffffe015a0b610
		  lr: 0xfffffff01d62d62c  fp: 0xffffffe015a0b620
		  lr: 0xfffffff01d063f28  fp: 0xffffffe015a0b990
		  lr: 0xfffffff01d064280  fp: 0xffffffe015a0b9e0
		  lr: 0xfffffff01de9a934  fp: 0xffffffe015a0ba00
		  lr: 0xfffffff01d7d53dc  fp: 0xffffffe015a0ba30
		  lr: 0xfffffff01d7c680c  fp: 0xffffffe015a0baa0
		  lr: 0xfffffff01d7c8734  fp: 0xffffffe015a0bb50
		  lr: 0xfffffff01d7c5f44  fp: 0xffffffe015a0bbe0
		  lr: 0xfffffff01d78d3a8  fp: 0xffffffe015a0bc10
		  lr: 0xfffffff01d59b5d8  fp: 0xffffffe015a0bc50
		  lr: 0xfffffff01d59ae5c  fp: 0xffffffe015a0bc90
		  lr: 0xfffffff01d638514  fp: 0x0000000000000000

