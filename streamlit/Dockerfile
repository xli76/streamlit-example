FROM python:3.6

WORKDIR /opt/dev

ADD requirements.txt .

RUN pip install -i https://mirrors.aliyun.com/pypi/simple/ -r requirements.txt;\
    rm -rf requirements.txt

CMD streamlit run app.py