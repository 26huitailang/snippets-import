# README

export dash snippets to raycast/snippetslab

## from dash

- 导出dash的snippets，是一个sqlite3文件，可以用sqlite3打开并查看
- 用py脚本读取并转换为对应的格式

dash snippets表格式

```json
[
    {
        "sid": 101,
        "title": "pam`",
        "body": "docker exec -it pam bash",
        "syntax": "None",
        "usageCount": 0
    }
]
```

raycast 模版

```json
[
  {
    "name": "Personal Email", "text": "sherlock@gmail.com", "keyword": "@@"
  },
  {
    "name": "Home Address", "text": "221B Baker St., London"
  },
  {
    "name": "Catchphrase 1", "text": "Elementary, my dear Watson", "keyword": "!elementary"
  }
]
```

snippetslab 模版

```json
{
  "contents": {
    "folders": [
      {
        "title": "Publishing",
        "uuid": "D3F0277B-6230-46C1-9D2E-3E1B8CE509BF"
      },
      {
        "title": "Graphic Design",
        "uuid": "D42BB115-44C4-4931-ACF8-8AD5F2D1778C",
        "children": [
          {
            "title": "Subfolder 1",
            "uuid": "4D356EC0-6118-4DDE-B09C-EC4116698877",
          },
          {
            "title": "Subfolder 2",
            "uuid": "2C6E47F2-A23F-4B4D-B63E-B1C37973A7BC",
          }
        ]
      }
    ],
    "snippets": [
      {
        "title": "Lorem ipsum",
        "folder": "D3F0277B-6230-46C1-9D2E-3E1B8CE509BF",
        "fragments": [
          {
            "title" : "Fragment",
            "language": "MarkdownLexer",
            "note": "Lorem ipsum is a placeholder text commonly used to demonstrate the visual form of a document or a typeface without relying on meaningful content.",
            "content": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.",
            "dateCreated": "2011-08-29T20:34:41Z",
            "dateModified": "2011-08-29T20:34:41Z",
            "uuid": "FA7BA77B-A93C-4D92-AC70-42EFF051C4D5",
          }
        ],
        "tags": [
          "017B7917-6B0A-4E9C-8757-F142E7B3C615",
          "D292ECB1-F007-4CE7-A65C-4AB08AD689FD"
        ],
        "dateCreated": "2011-08-29T20:34:41Z",
        "dateModified": "2011-08-29T20:34:41Z",
        "uuid": "5E680391-9BB0-4C8F-BC52-39F1836A717F",
      }
    ],
    "smartGroups": [
      {
        "title": "Markdown",
        "predicate": "ANY parts.language.displayName ==[cd] \"Markdown\"",
        "uuid": "41AD5A0A-84DE-4CD8-A951-7ED4060F7476",
      },
    ],
    "tags": [
      {
        "title": "lorem",
        "uuid": "017B7917-6B0A-4E9C-8757-F142E7B3C615",
      },
      {
        "title": "ipsum",
        "uuid": "D292ECB1-F007-4CE7-A65C-4AB08AD689FD",
      }
    ]
  }
}
```