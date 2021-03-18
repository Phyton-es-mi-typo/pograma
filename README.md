[![Build Status](https://travis-ci.org/Phyton-es-mi-typo/tyempo.svg?branch=main)](https://travis-ci.org/Phyton-es-mi-typo/tyempo)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![codecov](https://codecov.io/gh/Phyton-es-mi-typo/tyempo/branch/main/graph/badge.svg?token=6ZOR1TI4WY)](https://codecov.io/gh/Phyton-es-mi-typo/tyempo)

# tyempo

## Problem/Problema -> Epic/Épica :exclamation:

As [Notion](<https://www.notion.so/>) and Telegram users we would like to check a weather dashboard in Notion and get notified in Telegram daily or on demand.

Como usuarios de Notion y Telegram nos gustaría tener un dashboard del tiempo proporcionado por la AEMET y ser notificados en Telegram a diario o bajo demanda.

## Solution/Solución :bulb:

The solution we envision consists on an MVP application to solve the problem and will follow the philosophy of:

1. _make it work_
2. _make it right_
3. _make it fast_

This MVP application will itself consist of the following services in its most simple form that meets the required basic functionality.

- Weather Service (**WS**): A client of a public weather service that is agnostic to it, even if in the first implementation we can use AEMET's [weather API](https://opendata.aemet.es/centrodedescargas/AEMETApi?). This service will take the form of a REST API.

- Notion Service (**NS**): A client of the unofficial Notion API to interact with the Notion dashboard. This service will take the form of a REST API.

- Telegram Service (**TS**): _Bonus track_ a Telegram to get or push updates to the dashboard.

## Tools :wrench:

- Programming language: Python 3.8
- REST API Framework: We'd like to use [FastAPI](https://fastapi.tiangolo.com/) to implement a REST interface for our application's commmands.
- Web server: `uvicorn`
- APIs to consume: AEMET weather REST API and Notion API (through the unofficial SDK [notion-py](<https://github.com/jamalex/notion-py>))
- Best practices will include:
    - Testing: unit and functional
    - Logging (using the builtin `logging` module though `structlog` can be an alternative given time)
    - 12 factor principles, including configuration separation using 1) environment variables outside source control and eventually, time permitting `etcd` remote config
    - API docs
    - [`mask`](<https://github.com/jakedeichert/mask>)

- Configuration management/infrastructure layer: TBD

## Instrucciones / Instructions

We use Mask as Task Runner, to install it the information is [here](https://github.com/jakedeichert/mask#installation). `Mask` use `maskfile.md` for tasks declaration. But if you execute

```
maskfile.md test
```

It doesn't work, you need to execute

```
mask test
```

## Authors

[Cristóbal Contreras Rubio](<https://github.com/crisconru>)

[Jose M Rivera-Rubio](<https://github.com/jmrr>)

## Roadmap

- [x] Finish [curso-tdd milestones](<https://github.com/Phyton-es-mi-typo/tyempo/issues?q=label%3Acurso-tdd>)
- [ ] Finish [project milestones](<https://github.com/Phyton-es-mi-typo/tyempo/milestones>)
