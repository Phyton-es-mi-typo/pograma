# güeder

## Problem/Problema :exclamation:

We're [Notion](<https://www.notion.so/>) and Telegram users that would like to check a weather dashboard in Notion and get notified in Telegram daily or on demand.

Somos usuarios de Notion y Telegram que nos gustaría tener un dashboard del tiempo proporcionado por la AEMET y ser notificados en Telegram a diario o bajo demanda.

## Solution/Solución :bulb:

The solution we envision consists on an MVP application to solve the problem and will follow the philosophy of:

1. _make it work_
2. _make it right_
3. _make it fast_

This MVP application will itself consist of the following components in its most simple form that meets the required basic functionality.

- A client of the AEMET [weather API](<https://opendata.aemet.es/centrodedescargas/AEMETApi?>)

- A client of the unofficial Notion API to interact with the Notion dashboard.

- _Bonus track_ a Telegram to get or push updates to the dashboard.

## Tools

- Programming language: Python 3.8
- APIs to consume: AEMET weather REST API and Notion API (through the unofficial SDK [notion-py](<https://github.com/jamalex/notion-py>))
- Best practices will include:
    - Testing: unit and functional
    - Logging (using the builtin `logging` module though `structlog` can be an alternative given time)
    - 12 factor principles, including configuration separation using 1) environment variables outside source control and eventually, time permitting `etcd` remote config
    - API docs

## Authors

[Cristóbal Contreras Rubio](@crisconru)

[Jose M Rivera-Rubio](@jmrr)

