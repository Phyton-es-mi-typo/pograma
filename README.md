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

## Authors

[Cristóbal Contreras Rubio](<https://github.com/crisconru>)

[Jose M Rivera-Rubio](<https://github.com/jmrr>)

