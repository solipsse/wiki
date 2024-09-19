# system software

!!! term
    - multiprogrmming:

## os
!!! note "purpose"
    - kernel mode: optimise resource usage (all the key management) including io, memory, cpu
    - user mode: hide complexity from user
mode| memory and hardware access|error
-|:-:|-
kernel|O|may crash entire system
user|X|only affect the running application

### structure of os

layer|modular
:-:|:-:
![][layer]{ loading=lazy width=200 }|![][modular]{ loading=lazy width=200}

!!! note
    - layer: the lower layer need to be avaible and serve the higher level
    - modular: the kernel is always running to serve management task when required
### io system
!!! abstract
    ![][iosys]{ loading=lazy width=300}

    - os passes data between io passes to cpu directly
    - large data get passes to memory directly

### process management
!!! info
    - program:
    - process:
#### scheduling
!!! info
    - high-level-scheduler: select program from disk to memroy
    - medium-term scheduler: memory overcroweded -> take program back to disk
    - low-level-scheduler: select process to access cpu
#### scheduling method

### memory management
[video on segmentation vs paging][https://www.youtube.com/watch?v=p9yZNLeOj4s&pp=ygUkY29tcHV0ZXIgc2NpbmVjZSBwYWdpbmcgdnMgcGFydGl0aW9u]
!!! info
    - disk thrashing:
#### paging vs segmentation


[layer]: https://app.eraser.io/workspace/uy5XGTtYeOENCxYZsxjx/preview?elements=lz4YRhsgky4Fkw2LwgbJ4A&type=embed
[modular]: https://app.eraser.io/workspace/uy5XGTtYeOENCxYZsxjx/preview?elements=yXzYOBGcGtFB-kxQmEtaLQ&type=embed
[iosys]: https://app.eraser.io/workspace/uy5XGTtYeOENCxYZsxjx/preview?elements=YIDOHAr68VUYX4hdw5DKiQ&type=embed
