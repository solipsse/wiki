# system software

!!! term
	- multiprogramming
	- kernel mode
	- user mode
## os

| mode   | memory and hardware access | error                               |
| ------ | :------------------------: | ----------------------------------- |
| kernel |             O              | may crash entire system             |
| user   |             X              | only affect the running application |

OS can be thought of in two ways:
- layer: kernel and hardware run in lower layer allowing system call from the higher layer
- modular: kernel always run on the memory and other module perform a system call to kernel for attention

### io system
![][iosys]{loading=lazy width=200}

- os passes data between io passes to cpu directly
- large data get passes to memory directly

### process management
!!! info
    - program: static, written code
    - process: dynamic, the running program code

!!! state
    write this in term of the scheduling routine context chosen for marks

    - new: pcb being created for the process
    - ready: process on the memory waiting for cpu access/time to be executed
    - running: process execution by cpu
    - waiting/blocked: process waiting for io event so it can't be executed at that moment
    - terminated: process finished execution, (its memory space is recollected)

#### scheduling
!!! info
    - high-level-scheduler: select program from disk to memory (by user?)
    - medium-term scheduler: memory overcroweded -> take program back to disk
    - low-level-scheduler: select process to access cpu
    - priority-based: e.g. sjf, srtf
    - preemtive method: if the scheduling allow some sense of halting the process e.g. round robin
!!! method
    priority based: require calculation and reevaluation of priority (may be less performant)

    - sjf
    - srtf

    non priority based:

    - fcfs(fifo)
    - round robin


### memory management
[video on segmentation vs paging](https://www.youtube.com/watch?v=p9yZNLeOj4s&pp=ygUkY29tcHV0ZXIgc2NpbmVjZSBwYWdpbmcgdnMgcGFydGl0aW9u)
!!! info
    - disk thrashing: happen in paging, when it is requires to make many swap between physical memory and virtual memoryy
#### paging vs segmentation


[layer]: https://app.eraser.io/workspace/uy5XGTtYeOENCxYZsxjx/preview?elements=lz4YRhsgky4Fkw2LwgbJ4A&type=embed
[modular]: https://app.eraser.io/workspace/uy5XGTtYeOENCxYZsxjx/preview?elements=yXzYOBGcGtFB-kxQmEtaLQ&type=embed
[iosys]: https://app.eraser.io/workspace/uy5XGTtYeOENCxYZsxjx/preview?elements=YIDOHAr68VUYX4hdw5DKiQ&type=embed
*[pcb]: process control block
*[fcfs]: first come first serve
*[fifo]: first in first out
*[srtf]: shortest remaining time first
*[sjf]: shortest job first
*[round robin]: all process have their chance of processing in a time slice
*[multiprogramming]: allows multiple programs to be loaded into memory and executed concurrently on a single processor
*[kernel mode]: optimise resource usage (all the key management) including io, memory, cpu
*[user mode]: hide complexity from user