import json
import sqlite3
import uuid

DASH_DATA = "dash.dash"


def fetch_data_from_sqlite(db_path, query):
    # 连接到 SQLite 数据库
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # 执行查询
    cursor.execute(query)
    columns = [description[0] for description in cursor.description]
    rows = cursor.fetchall()

    # 将查询结果转换为 JSON 格式
    result = []
    for row in rows:
        result.append(dict(zip(columns, row)))

    # 关闭数据库连接
    conn.close()

    return result


def convert2raycast(data):
    ret = []
    for item in data:
        ret.append(dict(name=item["title"], text=item["body"], keyword=item["title"]))
    with open("./raycast.json", "w") as f:
        f.write(json.dumps(ret, indent=2))


def convert2snippetslab(data):
    ret = {
        "contents": {
            "snippets": [],
            "tags": [{"title": k, "uuid": v} for k, v in TAGS.items()],
        }
    }

    for item in data:
        temp = dict(
            title=item["title"],
        )
        if item["tag"]:
            if TAGS.get(item["tag"]):
                temp["tags"] = [TAGS[item["tag"]]]
        temp["fragments"] = [
            {"content": item["body"], "language": SYNTAX_MAP.get(item["syntax"], None)}
        ]
        ret["contents"]["snippets"].append(temp)

    with open("snippets.json", "w") as f:
        f.write(json.dumps(ret, indent=2))


# dash -> pygments(snippetslab use)
SYNTAX_MAP = {
    "JavaScript": "JavaScript",
    "Python": "Python",
    "SQL": "SQL",
    "None": None,
    "Go": "Go",
    "Standard": None,
}

TAGS = {
    "jquery": "080a7d2a-6bf8-420d-948c-30d78f9d8de0",
    "sqlalchemy": "6dbc06fe-7fda-4252-9942-97be474f8de1",
    "linux": "57618510-634c-42cb-818d-35f9131f6b3e",
    "sql": "f6c990b4-09d6-4b9d-a773-8e5c13c5a0c6",
    "pgsql": "43da34f6-e3ba-44d9-b8d0-ce6d5c629bf7",
    "grafana": "62d870d8-ff09-4ec4-a404-579b7e3cc666",
    "brew": "faa96c87-26ef-4d97-8b9d-b77d59a5f8fd",
    "npm": "6776ea68-6e60-47e6-9a15-93dd4dee2901",
    "influxdb": "e7ef7013-592a-47f5-8963-e4e65cbc17d7",
    "git": "3cfdea32-2ba4-435d-ac94-ea4f1f92c3cf",
    "C": "59cc3a9e-08ba-4c37-b47a-c9938d9037a9",
    "flask": "8229e519-764a-4bf0-be16-2370f3f7aa87",
    "httpie": "1395f413-48b4-43fb-9900-528ae1af5cea",
    "vim": "6bab0604-e256-4526-b890-50c26b0554d1",
    "vscode": "aaf89bff-9df5-4caa-a558-389980a703bf",
    "curl": "6ce93fe4-a71d-4404-8210-665fd964e7ba",
    "ah": "077ec24e-5d2c-4ef5-b9fa-faabd2bb310a",
    "golang": "85bc1a1b-4523-4392-a555-6581ee86bc40",
    "py_project": "06373754-2d38-465f-aa64-43c69979a976",
    "node": "c1731f4b-131b-4037-b1e6-70e9a2e32e6e",
    "python": "b474da8f-0cfb-405c-8d02-9323f35df7b9",
    "tree": "19f12cc7-945e-4783-9f19-8c886aad63b9",
    "django": "77e37286-a9bb-40c8-914a-e926cb7d1465",
}


def main():
    data = fetch_data_from_sqlite(
        DASH_DATA,
        "select title, body, syntax, tag from snippets left join tagsIndex on tagsIndex.sid == snippets.sid left join tags on tags.tid == tagsIndex.tid ;",
    )
    print(data)
    syntax = set([x["syntax"] for x in data])
    print(f"syntax: {syntax}")
    tags = set([x["tag"] for x in data])
    print(f"tags: {tags}")
    print({x: uuid.uuid4().__str__() for x in tags})
    with open("temp.json", "w") as f:
        f.write(json.dumps(data, indent=2))

    convert2raycast(data)
    convert2snippetslab(data)


if __name__ == "__main__":
    main()
