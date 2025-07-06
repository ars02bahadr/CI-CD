# CI/CD ve DevOps Araçları Rehberi

Bu proje, modern yazılım geliştirme süreçlerinde kullanılan CI/CD (Continuous Integration/Continuous Deployment) ve DevOps araçlarının kullanımını göstermektedir.

## 📋 İçindekiler

- [CI/CD Nedir?](#cicd-nedir)
- [DevOps Araçları](#devops-araları)
- [Docker](#docker)
- [GitHub Actions](#github-actions)
- [Jenkins](#jenkins)
- [Kubernetes](#kubernetes)
- [ArgoCD](#argocd)
- [Araçların Karşılaştırması](#araların-karşılaştırması)
- [Proje Yapısı](#proje-yapısı)
- [Kurulum ve Kullanım](#kurulum-ve-kullanım)

## 🔄 CI/CD Nedir?

### Continuous Integration (Sürekli Entegrasyon)
**CI**, geliştiricilerin kodlarını sık sık (günde birkaç kez) ana kod deposuna entegre etmesi ve her entegrasyonda otomatik testlerin çalıştırılması sürecidir.

**Faydaları:**
- Hataların erken tespit edilmesi
- Kod kalitesinin artması
- Entegrasyon sorunlarının azalması
- Geliştirme sürecinin hızlanması

**Tipik CI Adımları:**
1. Kod commit/push
2. Otomatik build
3. Unit testlerin çalıştırılması
4. Code quality check (linting)
5. Security scanning
6. Build artifact'larının oluşturulması

### Continuous Deployment (Sürekli Dağıtım)
**CD**, test edilmiş ve onaylanmış kodun otomatik olarak production ortamına dağıtılması sürecidir.

**Faydaları:**
- Manuel deployment hatalarının önlenmesi
- Hızlı feature delivery
- Rollback kolaylığı
- Deployment süreçlerinin standardizasyonu

**Tipik CD Adımları:**
1. Staging ortamına deployment
2. Integration testlerin çalıştırılması
3. Production ortamına deployment
4. Health check'lerin yapılması
5. Monitoring ve alerting

## 🛠️ DevOps Araçları

### Docker
**Docker**, uygulamaları container'lar içinde paketlemek, dağıtmak ve çalıştırmak için kullanılan bir platformdur.

**Ne İşe Yarar:**
- Uygulama izolasyonu
- Taşınabilirlik (portability)
- Tutarlı ortamlar
- Kaynak optimizasyonu
- Microservices mimarisi desteği

**Temel Komutlar:**
```bash
# Image oluşturma
docker build -t uygulama-adi .

# Container çalıştırma
docker run -p 8000:8000 uygulama-adi

# Container'ları listeleme
docker ps

# Container'ı durdurma
docker stop container-id

# Image'ları listeleme
docker images

# Container loglarını görme
docker logs container-id

# Container'a bağlanma
docker exec -it container-id bash
```

**Dockerfile Örneği:**
```dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 8000
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
```

### GitHub Actions
**GitHub Actions**, GitHub repository'lerinde CI/CD pipeline'ları oluşturmak için kullanılan bir servistir.

**Ne İşe Yarar:**
- GitHub ile entegre CI/CD
- YAML tabanlı workflow tanımları
- Marketplace'den hazır action'lar
- Matrix build desteği
- Self-hosted runner desteği

**Temel Yapı:**
```yaml
name: CI/CD Pipeline
on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v4
    - name: Set up Python
      uses: actions/setup-python@v4
      with:
        python-version: '3.11'
    - name: Run tests
      run: |
        pip install -r requirements.txt
        pytest
```

**Avantajları:**
- GitHub ile tam entegrasyon
- Kolay kurulum
- Ücretsiz plan mevcut
- Geniş ekosistem

**Dezavantajları:**
- GitHub'a bağımlılık
- Sınırlı özelleştirme
- Build süreleri

### Jenkins
**Jenkins**, açık kaynak kodlu bir CI/CD server'ıdır.

**Ne İşe Yarar:**
- Self-hosted CI/CD
- Plugin ekosistemi
- Pipeline as Code (Jenkinsfile)
- Distributed build desteği
- Çoklu proje desteği

**Jenkinsfile Örneği:**
```groovy
pipeline {
    agent any
    
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        
        stage('Build') {
            steps {
                sh 'docker build -t myapp .'
            }
        }
        
        stage('Test') {
            steps {
                sh 'docker run myapp pytest'
            }
        }
        
        stage('Deploy') {
            steps {
                sh 'docker push myapp:latest'
            }
        }
    }
}
```

**Kurulum Komutları:**
```bash
# Docker ile Jenkins kurulumu
docker run -p 8080:8080 -p 50000:50000 \
  -v jenkins_home:/var/jenkins_home \
  jenkins/jenkins:lts

# Jenkins CLI kurulumu
wget http://localhost:8080/jnlpJars/jenkins-cli.jar
java -jar jenkins-cli.jar -s http://localhost:8080 help
```

**Avantajları:**
- Tam kontrol
- Geniş plugin ekosistemi
- Self-hosted
- Ücretsiz

**Dezavantajları:**
- Kurulum ve yapılandırma karmaşıklığı
- Bakım gerektirir
- Kaynak tüketimi

### Kubernetes
**Kubernetes (K8s)**, container'ları yönetmek için kullanılan açık kaynak kodlu bir orchestration platformudur.

**Ne İşe Yarar:**
- Container orchestration
- Auto-scaling
- Load balancing
- Service discovery
- Rolling updates
- Health monitoring

**Temel K8s Bileşenleri:**
- **Pod**: En küçük deployable unit
- **Service**: Pod'lara erişim sağlar
- **Deployment**: Pod'ların yaşam döngüsünü yönetir
- **ConfigMap/Secret**: Konfigürasyon yönetimi
- **Ingress**: External erişim

**Temel Komutlar:**
```bash
# Cluster bilgilerini görme
kubectl cluster-info

# Pod'ları listeleme
kubectl get pods

# Service'leri listeleme
kubectl get services

# Deployment oluşturma
kubectl apply -f deployment.yaml

# Pod loglarını görme
kubectl logs pod-name

# Pod'a bağlanma
kubectl exec -it pod-name -- bash

# Service'e port forwarding
kubectl port-forward service/service-name 8080:80
```

**Deployment YAML Örneği:**
```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: myapp-deployment
spec:
  replicas: 3
  selector:
    matchLabels:
      app: myapp
  template:
    metadata:
      labels:
        app: myapp
    spec:
      containers:
      - name: myapp
        image: myapp:latest
        ports:
        - containerPort: 8000
```

### ArgoCD
**ArgoCD**, Kubernetes için GitOps tabanlı bir continuous delivery tool'udur.

**Ne İşe Yarar:**
- GitOps workflow
- Kubernetes manifest yönetimi
- Multi-cluster deployment
- Rollback capabilities
- Application health monitoring

**Temel Özellikler:**
- Git repository'den otomatik sync
- Declarative application management
- Multi-environment support
- RBAC (Role-Based Access Control)

**Kurulum:**
```bash
# ArgoCD kurulumu
kubectl create namespace argocd
kubectl apply -n argocd -f https://raw.githubusercontent.com/argoproj/argo-cd/stable/manifests/install.yaml

# ArgoCD CLI kurulumu
curl -sSL -o argocd-linux-amd64 https://github.com/argoproj/argo-cd/releases/latest/download/argocd-linux-amd64
sudo install -m 555 argocd-linux-amd64 /usr/local/bin/argocd
rm argocd-linux-amd64

# Admin şifresini alma
kubectl -n argocd get secret argocd-initial-admin-secret -o jsonpath="{.data.password}" | base64 -d
```

**Application YAML Örneği:**
```yaml
apiVersion: argoproj.io/v1alpha1
kind: Application
metadata:
  name: myapp
  namespace: argocd
spec:
  project: default
  source:
    repoURL: https://github.com/username/repo
    targetRevision: HEAD
    path: k8s
  destination:
    server: https://kubernetes.default.svc
    namespace: myapp
  syncPolicy:
    automated:
      prune: true
      selfHeal: true
```

## 🔄 Araçların Karşılaştırması

| Özellik | GitHub Actions | Jenkins | ArgoCD |
|---------|---------------|---------|---------|
| **Kurulum** | Hazır | Manuel | Orta |
| **Maliyet** | Ücretsiz plan | Ücretsiz | Ücretsiz |
| **Entegrasyon** | GitHub | Çoklu | Kubernetes |
| **Özelleştirme** | Sınırlı | Yüksek | Orta |
| **Bakım** | Yok | Yüksek | Orta |
| **Öğrenme Eğrisi** | Düşük | Yüksek | Orta |

## 🏗️ Proje Yapısı

```
CI-CD/
├── app/
│   └── main.py              # FastAPI uygulaması
├── tests/
│   └── test_main.py         # Test dosyaları
├── k8s/
│   ├── deployment.yaml      # Kubernetes deployment
│   ├── service.yaml         # Kubernetes service
│   └── ingress.yaml         # Kubernetes ingress
├── .github/
│   └── workflows/
│       └── ci-cd.yml        # GitHub Actions workflow
├── Dockerfile               # Docker image tanımı
├── .dockerignore           # Docker ignore dosyası
├── Jenkinsfile             # Jenkins pipeline
├── requirements.txt        # Python bağımlılıkları
└── README.md              # Bu dosya
```

## 🚀 Kurulum ve Kullanım

### 1. Lokal Geliştirme
```bash
# Bağımlılıkları yükleme
pip install -r requirements.txt

# Uygulamayı çalıştırma
uvicorn app.main:app --reload

# Testleri çalıştırma
pytest tests/
```

### 2. Docker ile Çalıştırma
```bash
# Image oluşturma
docker build -t myapp .

# Container çalıştırma
docker run -p 8000:8000 myapp

# Docker Compose ile
docker-compose up -d
```

### 3. Kubernetes Deployment
```bash
# Namespace oluşturma
kubectl create namespace myapp

# Deployment uygulama
kubectl apply -f k8s/

# Durumu kontrol etme
kubectl get all -n myapp
```

### 4. ArgoCD ile GitOps
```bash
# ArgoCD'ye bağlanma
argocd login localhost:8080

# Application oluşturma
argocd app create myapp --repo https://github.com/username/repo --path k8s --dest-server https://kubernetes.default.svc --dest-namespace myapp

# Sync etme
argocd app sync myapp
```

## 📊 Monitoring ve Logging

### Prometheus + Grafana
```yaml
# prometheus-config.yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: prometheus-config
data:
  prometheus.yml: |
    global:
      scrape_interval: 15s
    scrape_configs:
      - job_name: 'kubernetes-pods'
```

### ELK Stack (Elasticsearch, Logstash, Kibana)
```bash
# Elasticsearch kurulumu
kubectl apply -f https://download.elastic.co/downloads/eck/2.8.0/crds.yaml
kubectl apply -f https://download.elastic.co/downloads/eck/2.8.0/operator.yaml
```

## 🔒 Security Best Practices

### 1. Container Security
```dockerfile
# Non-root user kullanımı
RUN adduser --disabled-password --gecos '' appuser
USER appuser
```

### 2. Kubernetes Security
```yaml
# SecurityContext tanımı
securityContext:
  runAsNonRoot: true
  runAsUser: 1000
  capabilities:
    drop:
      - ALL
```

### 3. Secret Management
```bash
# Kubernetes secret oluşturma
kubectl create secret generic myapp-secret \
  --from-literal=username=admin \
  --from-literal=password=secret123
```

## 📈 Performance Optimization

### 1. Docker Optimization
```dockerfile
# Multi-stage build
FROM python:3.11-slim as builder
COPY requirements.txt .
RUN pip install --user -r requirements.txt

FROM python:3.11-slim
COPY --from=builder /root/.local /root/.local
```

### 2. Kubernetes Resource Limits
```yaml
resources:
  requests:
    memory: "64Mi"
    cpu: "250m"
  limits:
    memory: "128Mi"
    cpu: "500m"
```

## 🎯 Sonuç

Modern yazılım geliştirme süreçlerinde CI/CD ve DevOps araçları vazgeçilmez hale gelmiştir. Bu araçlar:

- **Hız**: Daha hızlı deployment ve delivery
- **Güvenilirlik**: Tutarlı ve tekrarlanabilir süreçler
- **Kalite**: Otomatik test ve quality check'ler
- **Ölçeklenebilirlik**: Microservices ve container tabanlı mimari
- **Güvenlik**: Otomatik security scanning ve compliance

Bu proje, bu araçların nasıl birlikte kullanılacağını göstermektedir. Her araç kendi güçlü yanlarına sahiptir ve projenizin ihtiyaçlarına göre seçim yapılmalıdır.

---

**Not**: Bu README dosyası sürekli güncellenmektedir. Yeni araçlar ve best practice'ler eklenecektir. 