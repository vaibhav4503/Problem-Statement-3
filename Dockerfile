FROM python

WORKDIR /telecomchurn

EXPOSE 8501

COPY . /telecomchurn

RUN pip install -r requirements.txt

CMD streamlit run server1.py