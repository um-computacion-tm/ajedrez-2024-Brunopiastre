FROM python:3-alpine

RUN apk add --no-cache git
RUN git clone git@github.com:um-computacion-tm/ajedrez-2024-Brunopiastre.git

WORKDIR /ajedrez-2024-Brunopiastre.git

RUN pip install -r requirements.txt

CMD ["sh", "-c", "coverage run -m unittest && coverage report -m && python main.py"]

# docker buildx build -t first-circleci-dqmdz-um .
# docker run -i first-circleci-dqmdz-um