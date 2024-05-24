from . import db
from datetime import datetime

class Word(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    swedish_word = db.Column(db.String(50), nullable=False)
    english_translation = db.Column(db.String(50), nullable=False)
    tags = db.Column(db.String(100))
    correct_count = db.Column(db.Integer, default=0)
    incorrect_count = db.Column(db.Integer, default=0)

    def __repr__(self):
        return f'<Word {self.swedish_word}>'

class QuizAttempt(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    word_id = db.Column(db.Integer, db.ForeignKey('word.id', ondelete='CASCADE'), nullable=False)
    was_correct = db.Column(db.Boolean, nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

    word = db.relationship('Word', backref=db.backref('attempts', lazy=True, cascade="all, delete-orphan"))

    def __repr__(self):
        return f'<QuizAttempt {self.word_id} {self.was_correct} {self.timestamp}>'
