TASK 1 - CREATE HELM CHARTS FOR KUBERNETS MANIFEST FILES

helm/
└── devops-api/
    ├── Chart.yaml
    ├── values.yaml
    └── templates/
        ├── deployment.yaml
        ├── service.yaml
        ├── configmap.yaml
        └── hpa.yaml

Task 1.1 — გადაიტანე კონფიგურაციები values.yaml-ში
მაგალითად, Chart-მა უნდა მოგცეს საშუალება, შეცვალო:
- Docker Image-ის სახელი და Tag.
- Replica-ების რაოდენობა.
- CPU და Memory Limits.
- Service-ის პორტები.
- გარემოს სახელი.
- HPA-ს მინიმალური და მაქსიმალური Replica-ების რაოდენობა.

---

TASK 2 - CREATE GITHUB WORFLOWS 

Phase 4 — CI Pipeline GitHub Actions-ით
მიზანი: კოდის ყოველი Push-ის შემდეგ ავტომატურად გაეშვას ტესტები და შეიქმნას Docker Image.

შექმენი:
.github/
└── workflows/
    └── ci.yaml

შენი ტასკებია:
1. Workflow გაეშვას Pull Request-ზე და მთავარ Branch-ზე Push-ისას.
2. დაყენდეს Python.
3. დაინსტალირდეს დამოკიდებულებები.
4. გაეშვას pytest.
5. შესრულდეს Docker Image-ის Build.
6. Image აიტვირთოს GitHub Container Registry-ში (GHCR).
მაგალითად, Image-ის სახელი შეიძლება იყოს:
ghcr.io/your-username/devops-api:latest

თუმცა უკეთესია, გამოიყენო უნიკალური Tag, მაგალითად Git Commit-ის SHA, რათა სხვადასხვა Build-ის Image-ები ერთმანეთში არ აგერიოს.

ფაზის დასრულების კრიტერიუმი: GitHub-ზე Push-ის შემდეგ Pipeline ავტომატურად გაეშვება და წარმატებულ Build-ზე Image Registry-ში გამოჩნდება.

დოკუმენტაცია: GitHub Actions Documentation.
